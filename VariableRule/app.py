from flask import Flask
from markupsafe import escape

app = Flask(__name__)
@app.route('/user/<username>')
def user_username(username):
    return 'Hello %s' %escape(username)

@app.route('/userid/<Int:userId')
def user_userid(userId):
    return 'Hello %s' %userId

@app.route('/userpath/<userPath')
def user_pathid(userPath):
    return 'Hell %s' %escape(userPath)