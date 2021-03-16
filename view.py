from flask import Flask
import model
from flask import Flask
import model
from flask import render_template
import sqlite3 as sl3

app = Flask(__name__)



@app.route('/')  # app routes to various html pages that we have assigned it to
def home_route():
    return render_template("home.html", model=model.setup())



