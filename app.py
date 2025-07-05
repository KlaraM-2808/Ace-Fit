from flask import Flask, render_template, request 
import sqlite3 

app = Flask(__name__)

#URL app responds to, when someone visits '/'(homepage) flask runs home() 
@app.route("/")
def home():
    return 'Welcome to AceFit.' 

if __name__ == "__main__":
    app.run(debug=True) 