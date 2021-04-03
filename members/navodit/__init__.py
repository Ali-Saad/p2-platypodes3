from flask import Blueprint, render_template, Flask, request
import model
from members.navodit import tri

members_navodit_bp = Blueprint('navodit', __name__, static_folder="bp_static", template_folder="templates")


@members_navodit_bp.route("/")
def navodit():
    return render_template("navo.html", model=model.setup())


@members_navodit_bp.route("/pythagorean")
def classes():
    return render_template("Pythagorean.html", model=model.setup())


@members_navodit_bp.route('/submitSides', methods=['POST'])
def submitSides():
    side1 = float(request.args.get("side1"))
    side2 = float(request.args.get("side2"))
    hypo = float(request.args.get("hypo"))
    jsonStr = tri.calculateSides(side1, side2, hypo)
    print(jsonStr)
    return jsonStr
