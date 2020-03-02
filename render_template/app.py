from flask import Flask, render_template


app = Flask(__name__)

@app.route('/hello/')
def note():
    return 'Hello world'

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

