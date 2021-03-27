from flask import Blueprint, render_template, Flask
import model


members_ali_bp = Blueprint('ali', __name__, static_folder="static", template_folder="templates")


@members_ali_bp.route("/")
def ali():
    return render_template("ali.html", model=model.setup())