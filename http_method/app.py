from flask import Flask, url_for, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/login', methods=['POST','GET'])
def main_login():
    if request.method == 'POST':
        return 'POSTING'
    else:
        return 'It\'s GETTING'
