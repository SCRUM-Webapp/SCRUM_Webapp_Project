from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager, login_user, login_required, logout_user
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
    return render_template('base.html')

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
            return redirect(url_for('product_backlog'))
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

        # Check if user already exists
        user = User.query.filter_by(email=email).first()
        if user:
            flash('This Email address already exists.')
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
    tickets = db.session.query(Ticket).order_by(Ticket.ticket_id).all()
    #tickets = db.session.execute(db.select(Ticket).order_by(Ticket.ticket_id)).fetchall()
    tickets2 = db.session.execute(db.select(Ticket).order_by(Ticket.ticket_id))
    print(tickets)
    #print(select(Ticket))
    print(type(tickets))

    print(tickets2)
    print(type(tickets2))

    # Convert the SQLAlchemy Row objects to a list of dictionaries
    #tickets_list = [dict(ticket) for ticket in tickets]

    # Pass the list of dictionaries to the template
    return render_template('Product_Backlog.html', tickets=tickets)
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

@app.route('/Sprint_Planning')
@login_required
def sprint_planning():
    return render_template('Sprint_Planning.html')

@app.route('/Profile')
@login_required
def profile():
    return render_template('Profile.html')

@app.route('/Logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))