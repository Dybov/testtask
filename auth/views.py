from flask import (
    render_template,
    redirect,
    request,
    session,
    flash,
    url_for,
    abort,
    g,
    jsonify,
)

import db

from auth import bp
from auth.model import User, Permission
from auth.utils import login_required, require_permission, is_ajax


@bp.route('/user/list')
@login_required
def user_list():
    users = User.query.all()

    def can_do_with_users(action):
        if g.user.is_superuser:
            return True
        perm = f'auth.model.User.{action}'
        return g.user.has_permission(perm)

    can = {
        'add': can_do_with_users('add'),
        'change': can_do_with_users('change'),
        'delete': can_do_with_users('delete'),
    }
    return render_template(
        'auth/user_list.html',
        users=users,
        can=can
    )


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


@bp.route('/user/add', methods=["GET", "POST"])
@require_permission('auth.model.User.add')
def add_user():
    if request.method == "POST":
        username = request.form.get('username')
        name = request.form.get('name')
        password = request.form.get('password')
        is_super = False

        if g.user.is_superuser:
            is_super = bool(request.form.getlist('is_superuser'))

        if username and password:
            user = User(
                username=username,
                password=password,
                name=name,
                is_superuser=is_super,
            )
            with db.db_session() as session:
                session.add(user)
                session.commit()
            return redirect(url_for('auth.user_list'))

        flash("Both username and password are required.")

    return render_template(
        'auth/user/add.html')


@bp.route('/user/<id>/change', methods=["GET", "POST"])
@require_permission('auth.model.User.change')
def change_user(id):
    user = User.query.get(id)
    if not user:
        abort(404)
    permissions = Permission.query.all()

    if request.method == "POST":
        username = request.form.get('username')
        name = request.form.get('name')

        if username:
            user.username = username
            user.name = name
            if g.user.is_superuser:
                is_super = bool(request.form.getlist('is_superuser'))
                user.is_superuser = is_super

            perm_from_form = request.form.getlist('permissions')
            with db.db_session() as db_session:
                for perm in permissions:
                    user_in = user in perm.users
                    if perm.model in perm_from_form:
                        if not user_in:
                            perm.users.append(user)
                    else:
                        if user_in:
                            perm.users.remove(user)
                    db_session.add(perm)
                db_session.add(user)
                db_session.commit()

            return redirect(url_for('auth.user_list'))

        flash("username is required field")

    return render_template(
        'auth/user/change.html', user=user, permissions=permissions)


@bp.route('/user/<id>/delete')
@require_permission('auth.model.User.delete')
def delete_user(id):
    user = User.query.get(id)
    if user == g.user:
        session.clear()

    with db.db_session() as db_session:
        db_session.delete(user)
        db_session.commit()

    if is_ajax():
        return jsonify(deleted=id)

    return redirect(url_for('auth.user_list'))
