import json
import math

from members.navodit.CRtTrig import RtTrig


def calculateSides(side1, side2, hypo):
    print("Inside tri. Values are", side1, side2, hypo)
    R = RtTrig()

    if not math.isnan(side2) and not math.isnan(hypo) :
        print("creating object with side2 and hypo with values ", side2, hypo)
        R.set_sides(side1, side2)
        R.set_sideAndHypo(side2, hypo)
    elif not math.isnan(side1)  and not math.isnan(hypo):
        print ("creating object with side1 and hypo with values ", side1, hypo)
        R.set_sideAndHypo(side1, hypo)
    elif not math.isnan(side1)  and not math.isnan(side2):
        print ("creating object with 2 side2 with values ", side1, side2)
        R.set_sides(side1, side2)

    print("Side 1: ", R.get_side1(), "Side 2: ", R.get_side2(), "Hypotenuse: ", R.get_hypo())
    print("Area = ", R.get_area())
    return R.serialize()
