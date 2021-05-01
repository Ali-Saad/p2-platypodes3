import json
import math
from json import JSONEncoder

from members.navodit.CRtTrig import RtTrig

triangleList = []


def calculateSides(side1, side2, hypo):
    print("Inside tri. Values are", side1, side2, hypo)
    R = RtTrig()
# selected based on two input values
    if not math.isnan(side2) and not math.isnan(hypo):
        print("creating object with side2 and hypo with values ", side2, hypo)
        R.set_sideAndHypo(side2, hypo)
    elif not math.isnan(side1) and not math.isnan(hypo):
        print("creating object with side1 and hypo with values ", side1, hypo)
        R.set_sideAndHypo(side1, hypo)
    elif not math.isnan(side1) and not math.isnan(side2):
        print("creating object with 2 side2 with values ", side1, side2)
        R.set_sides(side1, side2)
    print("Appending")
    triangleList.append(R)

    print("Side 1: ", R.get_side1(), "Side 2: ", R.get_side2(), "Hypotenuse: ", R.get_hypo())
    print("Area = ", R.get_area())
    return R.serialize()


def getSortedList():
    print("entering sorted list")
    triangleList.sort(reverse=True , key=lambda R: R.get_area())
    results = [obj.serialize() for obj in triangleList]
    jsdata = json.dumps({"results": results})
    result = jsdata.replace("\\", "")
    return result
