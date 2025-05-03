from flask_wtf import FlaskForm
from app.models import User
from app import db
import sqlalchemy as sa
import sqlalchemy.orm as so
from wtforms import EmailField, StringField, BooleanField, SubmitField, PasswordField, TextAreaField, ValidationError
from wtforms.validators import DataRequired, EqualTo, Length

class LoginForm(FlaskForm):
    username =  StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm = PasswordField('Confirm Password', validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField('Submit')

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(User.username == username.data))
        if user is not None:
            raise ValidationError('Please use a different username')

    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(User.email == email.data))
        if user is not None:
            raise ValidationError('Please use a different email')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About Me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    body = TextAreaField('Message', validators=[Length(min=0, max=140)])
    submit = SubmitField('Post')