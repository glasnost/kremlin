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

from math import ceil

class NewPostForm(Form):
    """ Post Form """
    name = TextField(u'Name', validators=[validators.required()])

    upload = FileField("Image File",
        validators=[
            file_required(),
            file_allowed(uploaded_images, "Not an image :("),
        ]
    )

    note = TextAreaField(u'Note/Comment', validators=[validators.optional()])

    tags = TextField(u'Tags (separated by space)',
            validators=[validators.optional()]
        )

class NewCommentForm(Form):
    """ Comment Form """
    name = TextField(u'Name', validators=[validators.required()])
    body = TextAreaField(u'Comment', validators=[validators.required()])

class LoginForm(Form):
    """ Login form for Kremlin application """
    username = TextField(u'Name', validators=[validators.required()])
    password = PasswordField(u'Password',
        validators=[validators.Required()]
    )

class RegisterForm(Form):
    """ Registration Form """
    username = TextField(u'Username',
        validators=[
            validators.Required(),
            validators.Length(min=3, max=25),
        ]
    )
    email = TextField(u'Email Address',
        validators=[
            validators.Required(),
            validators.Length(min=6, max=50),
            validators.Email(),
        ]
    )
    password = PasswordField(u'Password',
        validators = [
            validators.Required(),
            validators.EqualTo('confirm', message='Passwords must match!'),
        ]
    )
    confirm = PasswordField(u'Repeat Password')
#    accept_tos = BooleanField(u'I accept the TOS',
#        validators=[validators.Required()])

class Pagination(object):
    def __init__(self, page, per_page, total_count):
        self.page = page
        self.per_page = per_page
        self.total_count = total_count

    @property
    def pages(self):
        return int(ceil(self.total_count / float(self.per_page)))

    @property
    def has_prev(self):
        return self.page > 1

    @property
    def has_next(self):
        return self.page < self.pages

    def iter_pages(self, left_edge=2, left_current=2, right_current=5, right_edge=2):
        last = 0;
        for num in xrange(1, self.pages + 1):
            if num <= left_edge or \
                (num > self.page - left_current - 1 and \
                 num < self.page + right_current) or \
                num > self.pages - right_edge:
                    if last + 1 != num:
                        yield None
                    yield num
                    last = num