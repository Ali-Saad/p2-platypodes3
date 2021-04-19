import math
from json import JSONEncoder


class RtTrig:

    # Constructs object with all sides initialized to 0
    def __init__(self):
        self.__side1 = 0
        self.__side2 = 0
        self.__hypo = 0
        self.__area = 0

    # Getter for Side1
    def get_side1(self):
        return self.__side1

    # Getter for Side2
    def get_side2(self):
        return self.__side2

    # Getter for Hypo
    def get_hypo(self):
        return self.__hypo

    # sets values for Sides and calculate hypo
    def set_sides(self, val1, val2):
        self.__side1 = val1
        self.__side2 = val2
        self.__hypo = round(math.sqrt(self.__side1 ** 2 + self.__side2 ** 2), 2)
        self.__area = self.get_area();

    # sets values for Side and Hypo and calculate side
    def set_sideAndHypo(self, val2, hypo):
        self.__side2 = val2
        self.__hypo = hypo
        self.__side1 = round(math.sqrt(self.__hypo ** 2 - self.__side2 ** 2), 2)
        self.__area = self.get_area();

    def isRTValid(self):
        if self.__side1 == 0 or self.__side2 == 0 or self.__hypo == 0:
            return False
        else:
            return True

    def isEqual(self, trig):
        if (self.__side1 == trig.__side1 and self.__side2 == trig.__side2) or \
                (self.__side1 == trig.__side2 and self.__side2 == trig.__side1):
            return True
        else:
            return False

    def get_area(self):
        return round(0.5 * self.__side1 * self.__side2, 2)

    def serialize(self):
        return JSONEncoder().encode({
            'side1': self.__side1,
            'side2': self.__side2,
            'hypo': self.__hypo,
            'area': self.get_area()
        })
