import click
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import orm
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ticket_database.db' 

db = SQLAlchemy()
db.init_app(app) 

class Ticket(db.Model):
    __tablename__ = 'ticket'
    ticket_id = db.Column(db.Integer, primary_key=True, index=True)
    ticket_name = db.Column(db.String(80), nullable=False)
    sprint_number = db.Column(db.Integer) 
    workload = db.Column(db.Float)
    description = db.Column(db.Text)
    ticket_status = db.Column(db.String(12)) #done, in progress etc.

with app.app_context():
    db.create_all()

@click.command('init-db')
def init():  
    with app.app_context():
        db.drop_all()
        db.create_all()
        insert_sample()
    click.echo('Database has been initialized.')

app.cli.add_command(init)  #able to run flask init-db 

def insert_sample():
    # Delete all existing data, if any
    db.session.execute(db.delete(Ticket))
    

    # Create sample ticket items
    ticket1 = Ticket(ticket_id=1,ticket_name='Build logic to attach database to UI',sprint_number=1, workload=10, description='Needs to be implemented', ticket_status='in Progress')

    # Add all objects to the queue and commit them to the database
    db.session.add(ticket1)
    db.session.commit()
    """ db.session.add_all([todo1, todo2, todo3, todo4, todo5, list1, list2, list3])
    db.session.commit() """
