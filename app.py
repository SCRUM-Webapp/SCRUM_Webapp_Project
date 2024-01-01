from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm, RegisterForm, TicketForm
from sqlalchemy.exc import SQLAlchemyError


app = Flask(__name__)

from db import db, Ticket, User, insert_sample

app.config.from_mapping(
    SECRET_KEY = 'iterative_working_is_the_best',
    BOOTSTRAP_BOOTSWATCH_THEME = 'quartz'
)

bootstrap = Bootstrap5(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@login_required
def index():
    current_time = datetime.now()
    hour = current_time.hour

    if 4 <= hour < 12:
        time_of_day = 'morning'
    elif 12 <= hour < 18:
        time_of_day = 'afternoon'
    else:
        time_of_day = 'evening'
    return render_template('Index.html', username=current_user.username, time_of_day=time_of_day)

@app.route('/Login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # Retrieve form data
        email = form.email.data
        password = form.password.data

        # Validate credentials
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')

    return render_template('Login.html', form=form)

@app.route('/Register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        # Retrieve form data
        username = form.username.data
        email = form.email.data
        password = form.password.data

        # Check if username or email already exists
        existing_username = User.query.filter_by(username=username).first()
        existing_email = User.query.filter_by(email=email).first()

        if existing_username:
            flash('This username is already taken.')
        elif existing_email:
            flash('An account with that email already exists')
        else:
            # Create new user
            hashed_password = generate_password_hash(password)
            new_user = User(username=username, email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Your account has been succesfully created, please login.')
            return redirect(url_for('login'))
    return render_template('Register.html', form=form)

@app.route('/Ticket/New_Ticket')
@login_required
def new_ticket():
    return render_template('Ticket.html')

from sqlalchemy import inspect

@app.route('/Product_Backlog')
@login_required
def product_backlog():
    # Select all Tickets, order by ticket_id
    inbox_tickets = db.session.query(Ticket).filter_by(ticket_status='Inbox', sprint_number=None).order_by(Ticket.ticket_id).all()
    analyze_tickets = db.session.query(Ticket).filter_by(ticket_status='Analyze', sprint_number=None).order_by(Ticket.ticket_id).all()
    ready_for_sprint_tickets = db.session.query(Ticket).filter_by(ticket_status='Ready for Sprint', sprint_number=None).order_by(Ticket.ticket_id).all()
    next_sprint_tickets = db.session.query(Ticket).filter_by(ticket_status='Next Sprint', sprint_number=None).order_by(Ticket.ticket_id).all()

    #tickets = db.session.execute(db.select(Ticket).order_by(Ticket.ticket_id)).fetchall()
    #tickets2 = db.session.execute(db.select(Ticket).order_by(Ticket.ticket_id))
    #print(tickets)
    #print(select(Ticket))
    #print(type(tickets))

    #print(tickets2)
    #print(type(tickets2))

    # Convert the SQLAlchemy Row objects to a list of dictionaries
    #tickets_list = [dict(ticket) for ticket in tickets]

    # Pass the list of dictionaries to the template
    return render_template('Product_Backlog.html', inbox_tickets=inbox_tickets, analyze_tickets=analyze_tickets, ready_for_sprint_tickets=ready_for_sprint_tickets, next_sprint_tickets=next_sprint_tickets)
""" @app.route('/Product_Backlog')
@login_required
def product_backlog():
    #select all Tickets order by ticket_id convert to list because otherwise ChunkedIteratorResult Error when debugging
    tickets = db.session.execute(db.select(Ticket).order_by(Ticket.ticket_id))
    #pass the tickets to the template
    return render_template('Product_Backlog.html', tickets=tickets) """
    
@app.route('/Ticket/<int:ticket_id>')
@login_required
def ticket(ticket_id):
    return render_template('Ticket.html')

@app.route('/Sprint_Planning/<selected_sprint>')
@login_required
def sprint_planning(selected_sprint):
    if selected_sprint == 'add':
        # Handle the case when the user clicks on "+ Add Sprint"
        # This could be a separate route or logic depending on your requirements
        pass
    else:
        # Handle the case when a specific sprint is selected
        # You can use the selected_sprint parameter to filter tickets
        # and render the template accordingly
        sprint_number = int(selected_sprint)
        # Query tickets for the selected sprint
        to_do = db.session.query(Ticket).filter_by(ticket_status='To-Do', sprint_number=sprint_number).all()
        in_progress = db.session.query(Ticket).filter_by(ticket_status='In Progress', sprint_number=sprint_number).all()
        testing = db.session.query(Ticket).filter_by(ticket_status='Testing', sprint_number=sprint_number).all()
        finished_obsolete = db.session.query(Ticket).filter_by(ticket_status='Finished/Obsolete', sprint_number=sprint_number).all()
        
        return render_template('Sprint_Planning.html', selected_sprint=sprint_number, to_do=to_do, in_progress=in_progress, testing=testing, finished_obsolete=finished_obsolete)

@app.route('/Profile')
@login_required
def profile():
    return render_template('Profile.html')

@app.route('/Logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))