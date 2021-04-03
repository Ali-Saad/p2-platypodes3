from builtins import int

from flask import Blueprint, render_template, request
import model
from members.pragadeesh.pascal import Pascal

members_pragadeesh_bp = Blueprint('pragadeesh', __name__, static_folder="static", template_folder="templates")


@members_pragadeesh_bp.route("/")
def pragadeesh():
    return render_template("prag.html", model=model.setup())


@members_pragadeesh_bp.route("/pascal/", methods=["GET", "POST"])
def lab1():
    if request.form:
        return render_template("pascal.html", pascal=Pascal(int(request.form.get("row"))))
    return render_template("pascal.html", pascal=Pascal(25))
