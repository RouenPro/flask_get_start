from flask import Flask, request
app = Flask(__name__)

@app.route('/test')
def test():
    return 'Context Local'

with app.test_request_context('/test', method='GET'):
    assert request.path == '/test'
    assert request.method == 'GET'
