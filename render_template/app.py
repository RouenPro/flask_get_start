from flask import Flask, url_for, request, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def testing():
    return 'Haha'

@app.route('/login/')
def hehe():
    return render_template('hello.html')
    # return 'Hello'
