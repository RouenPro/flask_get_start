from flask import Flask
from markupsafe import escape

app = Flask(__name__)
@app.route('/')
def test():
    return 'R'

@app.route('/user/<float:number>')
def test_float(number):
    return 'This is float number %s' %escape(number)