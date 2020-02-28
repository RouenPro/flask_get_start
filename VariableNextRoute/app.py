from flask import Flask
from markupsafe import escape

app = Flask(__name__)
@app.route('/')
def test():
    return 'First welcome route'

@app.route('/user/<float:number>')
def test_float(number):
    return 'This is float number %s' %escape(number)

# UUID: fe4a3e33-cb4b-42ac-a29b-a8160a85af7e
@app.route('/usercode/<uuid:code_generator>')
def the_password(code_generator):
    return 'This is your password %s' %escape(code_generator)