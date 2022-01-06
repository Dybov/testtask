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
