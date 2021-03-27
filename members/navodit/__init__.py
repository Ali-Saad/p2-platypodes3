from flask import Blueprint, render_template, Flask
import model


members_navodit_bp = Blueprint('navodit', __name__, static_folder="static", template_folder="members")


@members_navodit_bp.route("/navo")
def navodit():
    return render_template("members/navodit/templates/navo.html", model=model.setup())


