import random


LEGSlist = ["Single Leg Squats", "Leg Press", "Bridges", "Split Squats", "Stairmaster", "Russian Deadlifts" ]


class LEGS:
    def __init__(self, series):
        if series < 0 or series > 6:
            raise ValueError("Series must be between 2 and 10")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        self.LEGS_series()


    #Wanted to do getters first since I struggle with them
    @property
    def series(self):
        return self._series

    @property
    def list(self):
        return self._list

    @property
    def number(self):
        return self._list[self._dictID - 1]

    def get_sequence(self, nth):
        return self._dict[nth]

    #ALGORITHM
    def LEGS_series(self):
        limit = self._series
        f = [(random.sample(LEGSlist, k=3))]  # changing k makes allows a larger limit for lists
        while limit > 0:
            self.set_data(f[0])
            f = [f[0]]
            limit -= 1

    def set_data(self, num):
        self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._dictID += 1

if __name__ == "__main__":
    #a represnts the value of testing
    a = 3
    legsrecs = LEGS(a / a)
    print(f"3 RANDOM LEG EXERCISES TO DO AT HOME = {legsrecs.list}")

#ARMS CODE (SAME AS LEGS)


ARMSlist = ["Bicep curls", "Tricep curls", "Hammer curls", "Dumbbell curls", "Overhead press"]

class ARMS:
    #Laying out all of the lists and dictionaries
    def __init__(self, series):
        if series < 0 or series > 5:
            raise ValueError("Series must be between 2 and 10")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        self.arms_series()



    #GETTERS
    @property
    def series(self):
        return self._series

    @property
    def list(self):
        return self._list

    @property
    def number(self):
        return self._list[self._dictID - 1]

    #Traditional Getter
    def get_sequence(self, nth):
        return self._dict[nth]


    def arms_series(self):
        limit = self._series
        f = [(random.sample(ARMSlist, k=3))]  #
        while limit > 0:
            self.set_data(f[0])
            f = [f[0]]
            limit -= 1


    def set_data(self, num):
        self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._dictID += 1

if __name__ == "__main__":
    '''Value for testing'''
    a = 3
    armsrecs = ARMS(a / a)
    print(f"3 RANDOM ARM EXERCISES TO DO AT HOME = {armsrecs.list}")

