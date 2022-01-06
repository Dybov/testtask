from flask import redirect, request, session, url_for

import functools


def login_required(func):
    """Redirect to login form unauthorized users"""

    # Copy function name, docstring of initial func and etc.
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('auth.login', next=request.endpoint))
        return func(*args, **kwargs)
    return wrapper
