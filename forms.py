from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms import validators
from wtforms.validators import DataRequired, Email

class ApplicationForm(FlaskForm):
    first_name = StringField('First name', [validators.Length(min=4, max=60)])
    second_name = StringField('Last name', [validators.Length(min=4, max=60)])
    phone = StringField('Phone')
    location = StringField('Location')
    application = TextAreaField('Details of incident')
    accept_tos = BooleanField('I consent to the processing of my data',
                              [DataRequired()])