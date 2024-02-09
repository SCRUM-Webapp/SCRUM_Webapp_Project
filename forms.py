from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, HiddenField, PasswordField, EmailField, IntegerField, FloatField, SelectField
from wtforms.validators import InputRequired, Length, Email, Optional

# form for user login
class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired(), Email(), Length(min=3, max=50)], render_kw={"placeholder": "Enter email"})
    password = PasswordField('Password', validators=[InputRequired(), Length(min=3, max=20)], render_kw={"placeholder": "Enter password"})
    submit = SubmitField('Login')

# form for user registration
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=3, max=20)], render_kw={"placeholder": "Enter username"})
    email = EmailField('Email', validators=[InputRequired(),Email(), Length(min=3, max=50)], render_kw={"placeholder": "Enter email"})
    password = PasswordField('Password', validators=[InputRequired(), Length(min=3, max=20)], render_kw={"placeholder": "Enter password"})
    submit = SubmitField('Register')

# form for creating and editing a ticket
class TicketForm(FlaskForm):
    ticket_name = StringField('Ticket_Name', validators=[InputRequired(), Length(min=3, max=30)])
    description = StringField('Description', validators=[InputRequired(), Length(min=3, max=300)], render_kw={"placeholder": "What is this ticket about?"})
    notes = StringField('Notes', render_kw={"placeholder": "Any additional informations?"})
    sprint_number = IntegerField('Sprint Number')
    workload = FloatField('Workload',validators=[Optional()])
    ticket_status = StringField('Ticket Status')

    #dropdown for choosing between product backlog and sprint planning
    product_sprint_select = SelectField('Product-Backlog/Sprint-Planning', choices=[
        ('productBacklog', 'Product-Backlog'),
        ('sprintPlanning', 'Sprint-Planning')
    ])
    #dropdown to choose between the backlog columns
    backlog_select = SelectField('Backlog Status', choices=[
        ('Inbox', 'Inbox'),
        ('Analyze', 'Analyze'),
        ('Ready for Sprint', 'Ready for Sprint'),
        ('Next Sprint', 'Next Sprint')
    ])
    #dropdown to choose between the sprint columns
    sprint_select = SelectField('Sprint Status', choices=[
        ('To-Do', 'To-Do'),
        ('In Progress', 'In Progress'),
        ('Testing', 'Testing'),
        ('Finished/Obsolete', 'Finished/Obsolete')
    ])
    #dropdown to select between the registered usernames to assign to a ticket
    owner_select = SelectField('Person working on this ticket', choices=[])
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #if the import is not outside of this function -> circular import error
        from db import User
        self.owner_select.choices = [(user.username, user.username) for user in User.query.all()]
    submit = SubmitField('Save')