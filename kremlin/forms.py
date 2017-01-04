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

from flask_wtf import Form, TextField, TextAreaField, FileField, \
        BooleanField, PasswordField, file_allowed, file_required, validators

from kremlin import uploaded_images

class NewPostForm(Form):
    """ Post Form """
    name = TextField('Name', validators=[validators.required()])

    upload = FileField("Image File",
        validators=[
            file_required(),
            file_allowed(uploaded_images, "Not an image :("),
        ]
    )

    note = TextAreaField('Note/Comment', validators=[validators.optional()])

    tags = TextField('Tags (separated by space)',
            validators=[validators.optional()]
        )

class NewCommentForm(Form):
    """ Comment Form """
    name = TextField('Name', validators=[validators.required()])
    body = TextAreaField('Comment', validators=[validators.required()])

class LoginForm(Form):
    """ Login form for Kremlin application """
    username = TextField('Name', validators=[validators.required()])
    password = PasswordField('Password',
        validators=[validators.Required()]
    )

class RegisterForm(Form):
    """ Registration Form """
    username = TextField('Username',
        validators=[
            validators.Required(),
            validators.Length(min=3, max=25),
        ]
    )
    email = TextField('Email Address',
        validators=[
            validators.Required(),
            validators.Length(min=6, max=50),
            validators.Email(),
        ]
    )
    password = PasswordField('Password',
        validators = [
            validators.Required(),
            validators.EqualTo('confirm', message='Passwords must match!'),
        ]
    )
    confirm = PasswordField('Repeat Password')
#    accept_tos = BooleanField(u'I accept the TOS',
#        validators=[validators.Required()])
