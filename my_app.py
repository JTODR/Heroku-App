from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello MasterCard</h1><h3>Joseph O'Donovan<\h3>"