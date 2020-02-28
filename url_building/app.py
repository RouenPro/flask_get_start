from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)
@app.route('/')
def main():
    return 'test'

# Testing the main function
with app.test_request_context():
    print(url_for('main'))