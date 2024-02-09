from datetime import datetime, timedelta
from flask import Flask, render_template, redirect, url_for, request, flash, abort
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm, RegisterForm, TicketForm
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import inspect

app = Flask(__name__)

from db import db, Ticket, User, insert_sample

app.config.from_mapping(
    SECRET_KEY = 'iterative_working_is_the_best',
    BOOTSTRAP_BOOTSWATCH_THEME = 'quartz',
    SESSION_COOKIE_SECURE = True,
    SESSION_COOKIE_HTTPONLY = True,
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
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
            # Redirect to update_user_list route to update choices
            return redirect(url_for('login'))
    return render_template('Register.html', form=form)

@app.route('/Product_Backlog')
@login_required
def product_backlog():
    # Select all Tickets, order by ticket_id
    inbox_tickets = db.session.query(Ticket).filter_by(ticket_status='Inbox', sprint_number=None).order_by(Ticket.ticket_id).all()
    analyze_tickets = db.session.query(Ticket).filter_by(ticket_status='Analyze', sprint_number=None).order_by(Ticket.ticket_id).all()
    ready_for_sprint_tickets = db.session.query(Ticket).filter_by(ticket_status='Ready for Sprint', sprint_number=None).order_by(Ticket.ticket_id).all()
    next_sprint_tickets = db.session.query(Ticket).filter_by(ticket_status='Next Sprint', sprint_number=None).order_by(Ticket.ticket_id).all()
    for ticket in inbox_tickets:
        print("Ticket ID:", ticket.ticket_id, "Assigned:", ticket.assigned)
    for ticket in analyze_tickets:
        print("Ticket ID:", ticket.ticket_id, "Assigned:", ticket.assigned)
    for ticket in ready_for_sprint_tickets:
        print("Ticket ID:", ticket.ticket_id, "Assigned:", ticket.assigned)
    for ticket in next_sprint_tickets:
        print("Ticket ID:", ticket.ticket_id, "Assigned:", ticket.assigned)

    return render_template('Product_Backlog.html', inbox_tickets=inbox_tickets, analyze_tickets=analyze_tickets, ready_for_sprint_tickets=ready_for_sprint_tickets, next_sprint_tickets=next_sprint_tickets)

@app.route('/Ticket/<int:ticket_id>', methods=['GET', 'POST'])
@login_required
def ticket(ticket_id):
    ticket = db.session.query(Ticket).filter_by(ticket_id=ticket_id).first()
    if not ticket:
        abort(404)

    form = TicketForm(request.form, obj=ticket)

    if form.validate_on_submit():
        form.populate_obj(ticket)

        ticket.assigned = form.owner_select.data

        if form.product_sprint_select.data == 'productBacklog':
            # Clear sprint-related fields
            ticket.sprint_number = None
            # Set ticket status based on the backlog selection
            ticket.ticket_status = form.backlog_select.data
        elif form.product_sprint_select.data == 'sprintPlanning':
            # Set ticket status based on the sprint selection
            if form.sprint_select.data == 'Finished/Obsolete':
                # If 'Finished/Obsolete' is selected, check which radio button is checked
                if request.form.get('btnradio') == 'Finished':
                    ticket.ticket_status = 'Finished'
                else:
                    ticket.ticket_status = 'Obsolete'
            else:
                ticket.ticket_status = form.sprint_select.data
            # Set sprint number
            ticket.sprint_number = form.sprint_number.data

        db.session.commit()

        # Redirect to product backlog or sprint planning based on the selection
        if form.product_sprint_select.data == 'productBacklog':
            return redirect(url_for('product_backlog'))
        else:
            return redirect(url_for('sprint_planning', selected_sprint=ticket.sprint_number))

    return render_template('Ticket.html', ticket=ticket, form=form)

@app.route('/Ticket/Delete/<int:ticket_id>', methods=['POST'])
@login_required
def delete_ticket(ticket_id):
    print(f"Attempting to delete ticket with ID: {ticket_id}")

    ticket = Ticket.query.get(ticket_id)
    if not ticket:
        print("Ticket not found.")
        abort(404, description='Ticket not found')

    db.session.delete(ticket)
    try:
        db.session.commit()
        print("Ticket deletion successful.")
    except Exception as e:
        print(f"Error occurred while deleting ticket: {e}")
        db.session.rollback()
        abort(500, description='Failed to delete ticket')
    return redirect(url_for('product_backlog'))

@app.route('/Ticket/New_Ticket', methods=['GET', 'POST'])
@login_required
def new_ticket():
    form = TicketForm(request.form)
    print("Choices for owner_select:", form.owner_select.choices)

    if form.validate_on_submit():
        new_ticket = Ticket()
        form.populate_obj(new_ticket)

        new_ticket.assigned = form.owner_select.data

        if form.product_sprint_select.data == 'productBacklog':
            # Set ticket status based on the backlog selection
            new_ticket.ticket_status = form.backlog_select.data
            new_ticket.sprint_number = None
            db.session.add(new_ticket)
            db.session.commit()
            #flash('New ticket added to Product Backlog')
            return redirect(url_for('product_backlog'))
        elif form.product_sprint_select.data == 'sprintPlanning':
            # Set ticket status based on the sprint selection
            new_ticket.sprint_number = form.sprint_number.data
            if form.sprint_select.data == 'Finished/Obsolete':
                # If 'Finished/Obsolete' is selected, check which radio button is checked
                if request.form.get('btnradio') == 'Finished':
                    new_ticket.ticket_status = 'Finished'
                else:
                    new_ticket.ticket_status = 'Obsolete'
            else:
                new_ticket.ticket_status = form.sprint_select.data
            db.session.add(new_ticket)
            db.session.commit()
            #flash('New ticket added to Sprint Planning')
            return redirect(url_for('sprint_planning', selected_sprint=new_ticket.sprint_number))
    elif request.method == 'POST' and (not form.ticket_name.data.strip() or not form.description.data.strip()):
        flash('Title and Description are required fields. Please fill them out.')

    return render_template('New_Ticket.html', form=form)

@app.route('/Sprint_Planning/<selected_sprint>')
@login_required
def sprint_planning(selected_sprint):
    if selected_sprint == 'add':
        pass
    else:
        sprint_number = int(selected_sprint)
        to_do = db.session.query(Ticket).filter_by(ticket_status='To-Do', sprint_number=sprint_number).all()
        in_progress = db.session.query(Ticket).filter_by(ticket_status='In Progress', sprint_number=sprint_number).all()
        testing = db.session.query(Ticket).filter_by(ticket_status='Testing', sprint_number=sprint_number).all()
        finished_obsolete = db.session.query(Ticket).filter(Ticket.ticket_status.in_(['Finished', 'Obsolete']), Ticket.sprint_number == sprint_number).all()


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