from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager


app = Flask(__name__)

from db import db, Ticket, insert_sample

app.config.from_mapping(
    BOOTSTRAP_BOOTSWATCH_THEME = 'quartz'
)

bootstrap = Bootstrap5(app)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/Login')
def login():
    return render_template('Login.html')

@app.route('/Register')
def register():
    return render_template('Register.html')

@app.route('/Ticket/New_Ticket')
def new_ticket():
    return render_template('Ticket.html')

@app.route('/Product_Backlog')
def product_backlog():
    return render_template('Product_Backlog.html')

@app.route('/Ticket/<int:ticket_id>')
def ticket(ticket_id):
    return render_template('Ticket.html')

@app.route('/Sprint_Planning')
def sprint_planning():
    return render_template('Sprint_Planning.html')

@app.route('/Profile')
def profile():
    return render_template('Profile.html')

@app.route('/Logout')
def logout():
    return redirect(url_for('login'))