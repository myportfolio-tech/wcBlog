from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validator=[DataRequired(), Length(min=5, max=20)])
    email = StringField('Email', validator=[DataRequired(), Email()])
    password = PasswordField('Password', validator=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password', validator=[DataRequired(), EqualTo('password')])

    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = StringField('Email', validator=[DataRequired(), Email()])
    password = PasswordField('Password', validator=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField("Login")
