class Color:
    def __init__(self, temp):
        int(temp)
        self._colorlist = []
        if temp > 200:
            print("red")
            self._colorlist.append("red")
        elif temp == 200:
            print("blue")
            self._colorlist.append("blue")
        else:
            print("green")
            self._colorlist.append("green")

    @property
    def colorlist(self):
        return self._colorlist


if __name__ == "__main__":
    temp = 200
    n = Color(temp)
    print(n.colorlist)
