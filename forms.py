from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, HiddenField, BooleanField, SelectField
from wtforms.validators import InputRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=3, max=20)])
    password = StringField('Password', validators=[InputRequired(), Length(min=3, max=20)])
    submit = SubmitField('Login')

class TicketForm(FlaskForm):
    ticket_id = HiddenField('Ticket ID')
    title = StringField('Title', validators=[InputRequired(), Length(min=3, max=20)])
    description = StringField('Description', validators=[InputRequired(), Length(min=3, max=20)])
    submit = SubmitField('Save')