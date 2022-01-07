"""ORM for auth blueprint."""
from werkzeug.security import check_password_hash, generate_password_hash

import db


class User(db.Base):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(300))
    name = db.Column(db.String(200))
    is_superuser = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, /, username, password, name='', is_superuser=False):
        self.username = username
        self.name = name
        self.is_superuser = is_superuser
        self.password = generate_password_hash(password)

    def check_password(self, password):
        if not self.username or not self.password:
            raise Exception('Impossible to check password of empty user')
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User Model "{self.username}">'

    def has_permission(self, permission):
        """Show if user has permission, but not check if superuser"""
        if isinstance(permission, str):
            permission = Permission.query.filter_by(model=permission).first()

        return self in permission.users


class Permission(db.Base):
    """Dynamic permission for changin models"""
    __tablename__ = 'permissions'
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), unique=True)
    users = db.relationship(
        'User',
        secondary='association_users_permissions',
        backref='permissions',
    )

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return f'<Permission Model "{self.model}">'

    @classmethod
    def prepopulate(cls):
        # Get permissions tree actions for all registred Models in ORM
        actions = ['add', 'change', 'delete']
        registry = db.Base.registry
        permission_models = [
            f'{mapper.class_.__module__}.{mapper.class_.__name__}.{action}'
            for mapper in registry.mappers
            for action in actions
            # skip Permission and UserPermission association
            if mapper.class_.__name__ not in (cls.__name__, 'UserPermission')
        ]

        # Remove permission_models that are not in current ORM
        models_to_remove = cls.query.filter(
            cls.model.notin_(permission_models)).all()

        # Retrieve permission_models that still in DB:
        stored_models_raw = cls.query.with_entities(cls.model).all()
        stored_models = [t.model for t in stored_models_raw]
        difference = set(permission_models).difference(stored_models)

        if not difference and not models_to_remove:
            return

        with db.db_session() as session:
            for model in difference:
                new = cls(model)
                session.add(new)
            for model in models_to_remove:
                session.delete(model)
            session.commit()


class UserPermission(db.Base):
    __tablename__ = 'association_users_permissions'
    user_id = db.Column(
        db.ForeignKey('users.id'),
        primary_key=True,
    )
    permission_id = db.Column(
        db.ForeignKey('permissions.id'),
        primary_key=True,
    )
