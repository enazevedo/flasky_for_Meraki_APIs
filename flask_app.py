
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/ifttt')
def ifttt_home():
    return 'Circulating. Nothing to see here at the home of IFTTT...'

