from flask import Blueprint, render_template, redirect, request, session

bp = Blueprint(
    'auth',
    __name__,
    url_prefix='/auth',
    template_folder='templates',
    static_folder='static',
)


@bp.route('/user-list')
def user_list():
    # Just temporary placeholder for user
    users = ['1', '2']
    return render_template('auth/user_list.html', users=users)


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        session.clear()
        session['username'] = request.form['username']
        return redirect(request.referrer)
    elif 'username' in session:
        return render_template('auth/relogin.html')
    return render_template('auth/login.html', next=request.args.get('next'))


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(request.url_root)
