from flask import flash, redirect, render_template,Blueprint, url_for
from flask_login import login_user, logout_user, login_required, current_user
from .forms import RegisterForm, LoginForm
from .models import User
from anoopdev import db

auth_view = Blueprint('auth', __name__, url_prefix='/auth',template_folder='templates')

@auth_view.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password1.data)
        print(f'check user: {user}')
        db.session.add(user)
        db.session.commit()
    
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'Error: { err_msg}',category='error')

    return render_template('auth/register.html',form=form)

@auth_view.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.validate_password(password_received=form.password1.data):
            login_user(user=user)
            flash(f'Logging successfull, logged in as {user.email}')
            return redirect(url_for("articles.articles"))
    return render_template('auth/login.html',form=form)

@auth_view.route('/logout')
def logout():
    logout_user()
    flash('User logged out')
    return redirect(url_for('home'))