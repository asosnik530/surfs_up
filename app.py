from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World'
export FLASK_APP=app.py
def math():
    return '2+2=4'
export FlASK_APP=app