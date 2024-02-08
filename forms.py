from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, HiddenField, PasswordField, EmailField, IntegerField, FloatField, SelectField
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
    #ticket_id = HiddenField('Ticket ID')
    ticket_name = StringField('Ticket_Name', validators=[InputRequired(), Length(min=3, max=30)])
    description = StringField('Description', validators=[InputRequired(), Length(min=3, max=100)], render_kw={"placeholder": "What is this ticket about?"})
    notes = StringField('Notes', render_kw={"placeholder": "Any additional informations?"})
    sprint_number = IntegerField('Sprint Number')
    workload = FloatField('Workload')
    ticket_status = StringField('Ticket Status')
    product_sprint_select = SelectField('Product-Backlog/Sprint-Planning', choices=[
        ('productBacklog', 'Product-Backlog'),
        ('sprintPlanning', 'Sprint-Planning')
    ])
    backlog_select = SelectField('Backlog Status', choices=[
        ('Inbox', 'Inbox'),
        ('Analyze', 'Analyze'),
        ('Ready for Sprint', 'Ready for Sprint'),
        ('Next Sprint', 'Next Sprint')
    ])
    sprint_select = SelectField('Sprint Status', choices=[
        ('To-Do', 'To-Do'),
        ('In Progress', 'In Progress'),
        ('Testing', 'Testing'),
        ('Finished/Obsolete', 'Finished/Obsolete')
    ])
    owner_select = SelectField('Person working on this ticket', choices=[])
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from db import User
        self.owner_select.choices = [(user.username, user.username) for user in User.query.all()]
    submit = SubmitField('Save')