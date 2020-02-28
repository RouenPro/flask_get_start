from flask import Flask

app = Flask(__name__)

@app.route('/')
def tested():
    return 'First route worked...'


