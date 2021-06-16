from flask import Blueprint, render_template, Flask, request
import model
from members.navodit import tri
from members.navodit import sort
from members.navodit.sort import listify

members_navodit_bp = Blueprint('navodit', __name__, static_folder="navo_bp", template_folder="templates")


@members_navodit_bp.route("/")
def navodit():
    return render_template("navo.html", model=model.setup())


@members_navodit_bp.route("/pythagorean")
def classes():
    return render_template("Pythagorean.html", model=model.setup())


@members_navodit_bp.route('/submitSides', methods=['POST'])
def submitSides():
    side1 = float(request.args.get("side1"))
    side2 = float(request.args.get("side2"))
    hypo = float(request.args.get("hypo"))

    jsonStr = tri.calculateSides(side1, side2, hypo)
    print(jsonStr)
    return jsonStr


@members_navodit_bp.route('/sorttriangles', methods=['POST'])
def sorttriangles():
    jsonStr = tri.getSortedList()
    print(jsonStr)
    return jsonStr


@members_navodit_bp.route('/bubblesort')
def sort():
    return render_template("bubblesort.html", model=model.setup())


@members_navodit_bp.route('/order', methods=['POST'])
def order():
    num = request.form['numbers']
    select = request.form['mySelect']
    sortedList = listify(num, select)
    return render_template("bubblesort.html", response=sortedList, model=model.setup())
