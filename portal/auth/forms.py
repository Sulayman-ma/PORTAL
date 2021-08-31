from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo, Regexp, ValidationError
from wtforms.fields import StringField, PasswordField, SubmitField
from ..models import User


class RegForm(FlaskForm):
    reg_number = StringField('Registeration Number: ', validators = [DataRequired()])
    first_name = StringField('First Name: ')
    last_name = StringField('Last Name: ')
    department = StringField('Department: ', validators = [DataRequired()])
    level = StringField('Level: ', validators = [DataRequired(), Regexp('^[0-9]{3}$')])
    password = PasswordField('Password: ', validators = 
                            [DataRequired(), EqualTo
                            ('password2', message = 'Passwords don\'t match')])
    password2 = PasswordField('Confirm Password: ', validators = [DataRequired()])
    submit = SubmitField('Sign Up')