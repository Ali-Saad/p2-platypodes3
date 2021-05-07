from flask import Blueprint, render_template, Flask
import model

members_ali_bp = Blueprint('ali', __name__, static_folder="static", template_folder="templates")

from builtins import int

from flask import Blueprint, render_template, request
import model
from members.ali.Aliminilab import Factorial
from members.ali.alibubblesort import alibubbleSort
##from members.ali.alibubblesort import list


@members_ali_bp.route("/")
def ali():
    return render_template("ali.html", model=model.setup())


@members_ali_bp.route("/Aliminilab", methods=["GET", "POST"])
def minilab():
    if request.form:
        return render_template("ali.html", minilab=Factorial(int(request.form.get("row"))))
    return render_template("ali.html", minilab=Factorial(5))

@members_ali_bp.route('/alibubbleSort')
def sort():
    return render_template("ali.html", model=model.setup())

@members_ali_bp.route("/sorted", methods=["POST"])
def order():
    if request.form:
        new=[]
        print("i have arrived")
        num = request.form['numbers']
        print(num)
        arr = num.split()
        print(arr)
        for i in range(len(arr)):
            new.append(int(arr[i]))
        print("new" + str(new))
       ##sortedList = list(num)
        sortedList = alibubbleSort(new)
        ##render_string=sortedList.string
        return render_template("ali.html", response=sortedList, minilab=Factorial(5))
    return render_template("ali.html")