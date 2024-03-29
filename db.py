import click
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import orm
from app import app
from flask_login import UserMixin

# configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ticket_database.db' 

# initialize SQLAlchemy with the flask app
db = SQLAlchemy()
db.init_app(app) 

# ticket table
class Ticket(db.Model):
    __tablename__ = 'ticket'
    ticket_id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    ticket_name = db.Column(db.String(80), nullable=False)
    sprint_number = db.Column(db.Integer) 
    workload = db.Column(db.Float)
    description = db.Column(db.Text)
    ticket_status = db.Column(db.String(17), default='Inbox') #Inbox, Analyze, Ready for Sprint, Next Sprint // To-Do, In Progress, Testing, Finished/Obsolete
    assigned = db.Column(db.String(30))
    notes = db.Column(db.Text)

# user table
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(128), nullable=False)

# create all tables
with app.app_context():
    db.create_all()

# CLI command to initalize the database
@click.command('init-db')
def init():  
    with app.app_context():
        db.drop_all()
        db.create_all()
    click.echo('Database has been initialized.')

#able to run flask init-db 
app.cli.add_command(init)  

def insert_sample():
    pass
