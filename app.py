from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

app.config.from_mapping(
    BOOTSTRAP_BOOTSWATCH_THEME = 'quartz'
)

from db import db, Ticket, insert_sample

bootstrap = Bootstrap5(app)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/Login')
def login():
    return render_template('Login.html')

@app.route('/Product_Backlog')
def product_backlog():
    return render_template('Product_Backlog.html')

@app.route('/Product_Backlog/<int:ticket_id>')
def ticket(ticket_id):
    return render_template('Ticket.html', ticket_id=ticket_id)

@app.route('/Sprint_Planning')
def sprint_planning():
    return render_template('Sprint_Planning.html')
