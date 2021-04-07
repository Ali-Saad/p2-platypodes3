from flask import Blueprint, render_template, Flask
import model


members_ali_bp = Blueprint('ali', __name__, static_folder="static", template_folder="templates")

from builtins import int

from flask import Blueprint, render_template, request
import model
from members.ali.Aliminilab import Factorial


@members_ali_bp.route("/")
def ali():
    return render_template("ali.html", model=model.setup())

@members_ali_bp.route("/Aliminilab/", methods=["GET", "POST"])
def minilab():
    if request.form:
        return render_template("ali.html", minilab=Factorial(int(request.form.get("row"))))
    return render_template("ali.html", minilab=Factorial(5))