from flask import (
    Blueprint,
    session,
    g,
    abort
)

from auth.model import User, Permission

bp = Blueprint(
    'auth',
    __name__,
    url_prefix='/auth',
    template_folder='templates',
    static_folder='static',
)


@bp.before_app_request
def load_user():
    if 'username' not in session:
        g.user = None
    else:
        user = User.query.filter_by(username=session['username']).first()
        if not user:
            session.clear()
            abort(500)
        g.user = user


@bp.before_app_first_request
def prepopulate_permission_db():
    Permission.prepopulate()
    import db
    with db.db_session() as session:
        usr = User.query.get(1)
        p = Permission.query.all()
        usr.permissions.extend(p)
        session.add(usr)
        session.commit()

# Ensure all views will be loaded
import auth.views
