from flask import Flask
import model
from flask import render_template
#import sqlite3 as sl3

app = Flask(__name__)



@app.route('/')  # app routes to various html pages that we have assigned it to
def home_route():
    return render_template("home.html", model=model.setup())

@app.route('/subscribe/')
def sub_route():
    return render_template("subscribe.html", model=model.setup())

@app.route('/aboutus/')
def about_route():
    return render_template("aboutus.html", model=model.setup())

@app.route('/lock/')
def lock_route():
    return render_template("lock.html", model=model.setup())

