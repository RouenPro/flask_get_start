from flask import Flask

app = Flask(__name__)

@app.route('/')
def tested():
    return 'First route worked...'

# Restriction behavior
@app.route('/project/')
def restriction():
    return 'No restriction path'

@app.route('/projects')
def restrictions():
    return 'It restriction of slash'
