from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World, this is a test!'

@app.route('/Product_Backlog')
def product_backlog():
    return render_template('Product_Backlog.html')