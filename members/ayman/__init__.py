from flask import Blueprint, render_template, Flask
import model

members_ayman_bp = Blueprint('ayman', __name__, static_folder="static", template_folder="templates")


@members_ayman_bp.route("/")
def ayman():
    return render_template("ayman.html", model=model.setup())