from flask import Blueprint, render_template, Flask
import model


members_ali_bp = Blueprint('ali', __name__, static_folder="static", template_folder="templates")

from builtins import int

from flask import Blueprint, render_template, request
import model
from members.ali.Aliminilab import Factorial
from members.ali.alibubblesort import bubbleSort


@members_ali_bp.route("/")
def ali():
    return render_template("ali.html", model=model.setup())

@members_ali_bp.route("/Aliminilab/", methods=["GET", "POST"])
def minilab():
    if request.form:
        return render_template("ali.html", minilab=Factorial(int(request.form.get("row"))))
    return render_template("ali.html", minilab=Factorial(5))

@members_ali_bp.route("/alibubblesort", methods=["GET", "POST"])
def bubblesort():
    if request.form:
        all_list = []
        b = 1 # to ensure first number is 0

        newbox_counter = request.form.get('newbox_counter')
        print('number of boxes added' +str(newbox_counter))

        numberToItterate = 5
        # iterating through all of the form text fields input
        for i in range(numberToItterate):
            string_used = 'user_input' + str(b)
            user_input = request.form.get(string_used)
            all_list.append(int(user_input))
            b = b + 1

        print(all_list)
        bubble = bubbleSort(all_list)
        return render_template("ali.html", active_page='ali', output_list = bubble)

    return render_template("ali.html", active_page='ali')