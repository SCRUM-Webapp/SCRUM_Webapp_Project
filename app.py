from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World, this is a test!'

@app.route('/product_backlog')
def product_backlog():
    return render_template('product_backlog.html')