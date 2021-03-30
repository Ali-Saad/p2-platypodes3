from flask import Blueprint, render_template, Flask
import model


members_navodit_bp = Blueprint('navodit', __name__, static_folder="bp_static", template_folder="templates")


@members_navodit_bp.route("/")
def navodit():
    return render_template("navo.html", model=model.setup())





