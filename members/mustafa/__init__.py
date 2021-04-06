from flask import Blueprint, render_template, Flask, request
import model


members_mustafa_bp = Blueprint('mustafa', __name__, static_folder="bp_static", template_folder="templates")


@members_mustafa_bp.route("/")
def mustafa():
    return render_template("mustafa.html", model=model.setup())