from wtforms import StringField, PasswordField, BooleanField
from flask_wtf import FlaskForm, form
from wtforms.validators import InputRequired, Email
from wtforms.widgets import TextArea

class SignupForm(FlaskForm):
    
    email = StringField('Email', validators=[InputRequired(), Email()])
    username = StringField('username',validators=[InputRequired()])   
    password = PasswordField('Password',validators=[InputRequired()])


class LoginForm(FlaskForm):
    username = StringField('Username',validators=[InputRequired()])
    password = PasswordField('Password',validators=[InputRequired()])
    remember = BooleanField('Remember') 
    

    