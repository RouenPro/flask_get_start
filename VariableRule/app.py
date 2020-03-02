from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/user/<username>')
def user_name(username):
    return 'This is %s' %escape(username)

@app.route('/userid/<int:userid>')
def user_id(userid):
    return 'This is userid %d' %userid


@app.route('/userpath/<path:userpath>')
def user_path(userpath):
    return 'This is userpath %s' %escape(userpath)

