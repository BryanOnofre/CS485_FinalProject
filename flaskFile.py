import pymongo
from flask import Flask, render_template, request
import hashlib
import uuid


# you will need to change this connection string to match your own instance
client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0-urwbg.mongodb.net/test?retryWrites=true&w=majority")
# remember that if you have special characters in your password, you need to "escape" them
# or import and use urllib.parse.quote_plus
# More info: https://pymongo.readthedocs.io/en/stable/examples/authentication.html
# Ascii codes: https://ascii.

app = Flask(__name__)

# render default index page
@app.route('/')
def index():
    return render_template('loginpage.html')

# render login page
@app.route('/loginpage')
def login():
    return render_template('loginpage.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8643)