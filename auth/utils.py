import functools

from flask import redirect, request, session, url_for, g, abort

from auth.model import Permission


def login_required(func):
    """Redirect to login form unauthorized users"""

    # Copy function name, docstring of initial func and etc.
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('auth.login', next=request.endpoint))
        return func(*args, **kwargs)
    return wrapper


def require_permission(permission_name):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not g.user:
                abort(403)

            if not g.user.is_superuser:
                perm_obj = Permission.query.filter_by(
                    model=permission_name).first()

                if not perm_obj:
                    raise Exception(
                        f'{permission_name} does not match any model in DB')

                if not g.user.has_permission(perm_obj):
                    abort(403)

            return func(*args, **kwargs)
        return wrapper
    return decorator
