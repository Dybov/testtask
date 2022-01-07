from flask import (
    render_template,
    redirect,
    request,
    session,
    flash,
    url_for,
)

from auth import bp
from auth.model import User
from auth.utils import login_required


@bp.route('/user-list')
@login_required
def user_list():
    users = User.query.all()
    return render_template('auth/user_list.html', users=users)


@bp.route('/login', methods=('GET', 'POST'))
def login():
    next_ = request.args.get('next') or request.url_root

    if request.method == 'POST':
        username = request.form['username']

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(request.form['password']):
            session.clear()
            session['username'] = username
            return redirect(url_for(next_))

        flash("Wrong username or password")

    elif 'username' in session:
        return render_template('auth/relogin.html')

    return render_template('auth/login.html', next=next_)


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(request.url_root)
