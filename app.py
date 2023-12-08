from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

app.config.from_mapping(
    BOOTSTRAP_BOOTSWATCH_THEME = 'quartz'
)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/Login')
def login():
    return render_template('Login.html')

@app.route('/Product_Backlog')
def product_backlog():
    return render_template('Product_Backlog.html')

@app.route('/Sprint_Planning')
def sprint_planning():
    return render_template('Sprint_Planning.html')