from flask_wtf import FlaskForm
from wtforms import EmailField,PasswordField,SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from .models import User

class RegisterForm(FlaskForm):
    
    def validate_email(self,email):
        user = User.query.filter_by(email=email)
        if user:
            raise ValidationError('Email alreay exist, try login or use another')
    
    email = EmailField(label="Email", validators=[Email(), DataRequired()])
    password1 = PasswordField(label="Password", validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label="Confirm Password", validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label="Register")

class LoginForm(FlaskForm):
    email = EmailField(label="Email", validators=[Email(), DataRequired()])
    password1 = PasswordField(label="Password", validators=[Length(min=6), DataRequired()])
    submit = SubmitField(label="Login")