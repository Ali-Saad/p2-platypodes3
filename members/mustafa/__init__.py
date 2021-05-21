from flask import Blueprint, render_template, Flask, request
import model
from members.mustafa.bubblesort import Bubblesort

members_mustafa_bp = Blueprint('mustafa', __name__, static_folder="bp_static", template_folder="templates")


@members_mustafa_bp.route("/", methods=["GET", "POST"])
def mustafa():
    if request.form:
        return render_template("mustafa.html", bubble=Bubblesort(request.form.get("sort")))
    return render_template("mustafa.html", bubble=Bubblesort("42, 7, 9, 2"))

