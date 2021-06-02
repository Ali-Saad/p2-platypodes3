from flask import Blueprint, render_template, Flask, request
import model
from members.ayman.lab1 import Factor
from members.ayman.bubbly import bubbleSort
from builtins import int

members_ayman_bp = Blueprint('ayman', __name__, static_folder="static", template_folder="templates")

@members_ayman_bp.route("/")
def ayman():
    return render_template("ayman.html", model=model.setup())

@members_ayman_bp.route("/lab1/", methods=["GET", "POST"])
def lab1():
    if request.form:
        return render_template("lab1.html", numpass = Factor(int(request.form.get("list"))))
    return render_template("lab1.html", numpass = Factor(50000))

@members_ayman_bp.route("/bubbles/", methods=["GET", "POST"])
def bubble():
    if request.form:
        return render_template("bubbly.html", bubble=bubbleSort(request.form.get("str")))
    return render_template("bubbly.html", bubble=bubbleSort("3,6,2,1,5,9"))
