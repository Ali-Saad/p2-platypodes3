from flask import Blueprint, render_template, Flask
import model


members_pragadeesh_bp = Blueprint('pragadeesh', __name__, static_folder="static", template_folder="templates")


@members_pragadeesh_bp.route("/")
def pragadeesh():
    return render_template("prag.html", model=model.setup())

@members_pragadeesh_bp.route("/pascal/")
def pascal():
    return render_template("pascal.html", model=model.setup())