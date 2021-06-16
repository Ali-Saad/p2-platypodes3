from flask import Blueprint, render_template
import model

members_deliverable_bp = Blueprint('deliverable', __name__, static_folder="static", template_folder="templates")


@members_deliverable_bp.route("/")
def deliverable():
    return render_template("deliverable.html", model=model.setup())
