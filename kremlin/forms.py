"""
               #   # ####  ##### #   # ##### #   # #   #
               #  #  #   # #     ## ##  #  # #  ## #   #
               ###   ####  ####  # # #  #  # # # # #####
               #  #  #     #     #   #  #  # ##  # #   #
               #   # #     ##### #   # #   # #   # #   #

                   Kremlin Magical Everything System
               Glasnost Image Board and Boredom Inhibitor

"""

""" Module containing form classes and validation, for use with WTForms """

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired

from wtforms import TextField, TextAreaField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Optional, Length, Email, \
        EqualTo

from kremlin import uploaded_images

class NewPostForm(FlaskForm):
    """ Post Form """
    name = TextField('Name', validators=[DataRequired()])

    upload = FileField("Image File",
        validators=[
            FileRequired(),
            FileAllowed(uploaded_images, "Not an image :("),
        ]
    )

    note = TextAreaField('Note/Comment', validators=[Optional()])

    tags = TextField('Tags (separated by space)',
            validators=[Optional()]
        )

class NewCommentForm(FlaskForm):
    """ Comment Form """
    name = TextField('Name', validators=[DataRequired()])
    body = TextAreaField('Comment', validators=[DataRequired()])

class LoginForm(FlaskForm):
    """ Login form for Kremlin application """
    username = TextField('Name', validators=[DataRequired()])
    password = PasswordField('Password',
        validators=[DataRequired()]
    )

class RegisterForm(FlaskForm):
    """ Registration Form """
    username = TextField('Username',
        validators=[
            DataRequired(),
            Length(min=3, max=25),
        ]
    )
    email = TextField('Email Address',
        validators=[
            DataRequired(),
            Length(min=6, max=50),
            Email(),
        ]
    )
    password = PasswordField('Password',
        validators = [
            DataRequired(),
            EqualTo('confirm', message='Passwords must match!'),
        ]
    )
    confirm = PasswordField('Repeat Password')
#    accept_tos = BooleanField(u'I accept the TOS',
#        validators=[validators.Required()])
