from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)
@app.route('/')
def main():
    return 'test'

@app.route('/login')
def logincheck_url():
    return 'Login successfully'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/userurl/<usernames>')
def usernames_check(usernames):
    return '{}\'s my fri' .format(escape(usernames))

# Testing the main function
with app.test_request_context():
    print(url_for('main'))
    print(url_for('logincheck_url'))
    print(url_for('logincheck_url', next='/'))
    print(url_for('show_user_profile',username='Chamrouen'))
    print(url_for('usernames_check', usernames='Rouen'))
    # print(url_for('show_user_profile',next='/'))
    # print(url_for('usernames_check', usernames='RouenPro'))