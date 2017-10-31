from flask import Flask

app = Flask(__name__)

@app.route('/')     #Tell flask what URL should trigger the function
def hello_mastercard():
    heading = "<h1>Hello MasterCard</h1>"
    subheading = "<h3>Joseph O'Donovan</h3>"
    return heading + subheading