from flask import Flask, request
app = Flask(__name__)
@app.route('/', methods=['POST'])
def result():
    print(request.form['a']) # should display '1'
    return 'Received !' # response to your request.
