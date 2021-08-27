from flask_wtf import FlaskForm
from flask_wtf.recaptcha import fields
from wtforms.validators import DataRequired, EqualTo, ValidationError
from wtforms.fields import StringField, PasswordField, SubmitField, BooleanField
from .models import User


class RegForm(FlaskForm):
    reg_number = StringField('Registeration Number: ', validators = [DataRequired()])
    first_name = StringField('First Name: ')
    last_name = StringField('Last Name: ')
    password = PasswordField('Password: ', validators = 
                            [DataRequired(), EqualTo
                            ('password2', message = 'Passwords don\'t match')])
    password2 = PasswordField('Confirm Password: ', validators = [DataRequired()])
    submit = SubmitField('Sign Up')

    @staticmethod
    def validate_reg_number(self, field):
        if User.query.filter_by(reg_number = field.data).first():
            raise ValidationError('User already registered.')
