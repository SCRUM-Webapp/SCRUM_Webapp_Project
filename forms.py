from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, HiddenField, PasswordField, EmailField
from wtforms.validators import InputRequired, Length, Email

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired(), Email(), Length(min=3, max=50)], render_kw={"placeholder": "Enter email"})
    password = PasswordField('Password', validators=[InputRequired(), Length(min=3, max=20)], render_kw={"placeholder": "Enter password"})
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=3, max=20)], render_kw={"placeholder": "Enter username"})
    email = EmailField('Email', validators=[InputRequired(),Email(), Length(min=3, max=50)], render_kw={"placeholder": "Enter email"})
    password = PasswordField('Password', validators=[InputRequired(), Length(min=3, max=20)], render_kw={"placeholder": "Enter password"})
    submit = SubmitField('Register')

class TicketForm(FlaskForm):
    ticket_id = HiddenField('Ticket ID')
    title = StringField('Title', validators=[InputRequired(), Length(min=3, max=30)])
    description = StringField('Description', validators=[InputRequired(), Length(min=3, max=100)])
    submit = SubmitField('Save')