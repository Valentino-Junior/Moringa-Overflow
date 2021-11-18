from flask import (render_template, redirect, url_for,flash, request)
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from ..models import User
from .forms import RegistrationForm, LoginForm, UpdateAccountForm
from .. import db
# from ..email import mail_message

@auth.route("/signup", methods = ["GET", "POST"])

def register():
    '''Function to register the user and commit it to the db'''
    signup_form = RegistrationForm()
    if signup_form.validate_on_submit():
        user = User(username = signup_form.username.data, 
                    email = signup_form.email.data,
                    password = signup_form.password.data)
        db.session.add(user)
        db.session.commit()

        # mail_message("Welcome to 60 seconds",   "email/welcome", user.email, user = user)
        
        return redirect(url_for("auth.login"))
    title = "Sign Up The-Blog"
    return render_template("auth/signup.html", form = signup_form, title = title)

@auth.route("/login", methods = ["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(request.args.get("next") or url_for("main.index"))

        flash("Invalid Username or Password or the user exists already")
    
    title = "Login to The-Blog"
    return render_template("auth/login.html", form = login_form,
                            title = title)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@auth.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        # if form.picture.data:
            # picture_file = save_picture(form.picture.data)
            # current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('auth.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    # image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', form=form)