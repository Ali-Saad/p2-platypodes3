from builtins import int

from flask import Blueprint, render_template, request
import model
from members.pragadeesh.bubblesort import bubbleSort
from members.pragadeesh.pascal import pascalTriangle

members_pragadeesh_bp = Blueprint('pragadeesh', __name__, static_folder="static", template_folder="templates")


@members_pragadeesh_bp.route("/")
def pragadeesh():
    return render_template("prag.html", model=model.setup())


@members_pragadeesh_bp.route("/pascal/", methods=["GET", "POST"])
def lab1():
    if request.form:
        return render_template("pascal.html", pascal=pascalTriangle(int(request.form.get("row"))))
    return render_template("pascal.html", pascal=pascalTriangle(0))


@members_pragadeesh_bp.route("/bubble/", methods=["GET", "POST"])
def lab2():
    if request.form:
        return render_template("pragadeesh/bubblesort.html", bubble=bubbleSort(request.form.get("str")))
    return render_template("pragadeesh/bubblesort.html", bubble=bubbleSort("2,9,5,7,3"))
