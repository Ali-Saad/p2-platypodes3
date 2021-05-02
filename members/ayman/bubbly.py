# Python program for implementation of Bubble Sort

'''class bblsort:

    def __init__(self, input, stri):
        self.finalc = []
        self.finaln = []
        self.numbers = []
        self.chars = []
        self._input = input
        self.sorterc(stri)
        self.sortern()


    def sortern(self):
        numberList = self._input
        for i in range(len(self.numbers)-1, 0, -1):
            for j in range(i):
                if self.numbers[j]>self.numbers[j+1]:
                    temp = self.numbers[j]
                    self.numbers[j] = self.numbers[j+1]
                    self.numbers[j+1] = temp
        self.finaln = numberList

    def sorterc(self, str):
        charList = self._input
        # Hash array to keep count of characters.
        # Initially count of all charters is
        # initialized to zero.
        MAX_CHAR = 26
        charCount = [0 for i in range(MAX_CHAR)]

        # Traverse string and increment
        # count of characters
        for i in range(0, len(str), 1):

            # 'a'-'a' will be 0, 'b'-'a' will be 1,
            # so for location of character in count
            # array we wil do str[i]-'a'.
            charCount[ord(str[i]) - ord('a')] += 1

        # Traverse the hash array and print
        # characters
        for i in range(0, MAX_CHAR, 1):
            for j in range(0, charCount[i], 1):
                print(chr(ord('a') + i), end = "")
        self.finalc = charList
    @property
    def input(self):
        return self._input

    @property
    def listn(self):
        return self.finaln

    @property
    def listc(self):
        return self.finalc

    @property
    def list(self):
        return self.final

if __name__ == '__main__':
    s = "geeksforgeeks"'''

class bubbleSort:
    def __init__(self, user_input):
        self._listO = list(map(int, user_input.split(",")))
        self._listS = self._listO.copy()
        self._listIter = []
        for i in range(len(self._listS) - 1, 0, -1):  # (6, -1, 0, -1)
            self._listIter.append(self._listS.copy())
            for j in range(i):
                if self._listS[j] > self._listS[j + 1]:
                    temp = self._listS[j]
                    self._listS[j] = self._listS[j + 1]
                    self._listS[j + 1] = temp


    @property
    def listS(self):
        return self._listS

    @property
    def listO(self):
        return self._listO

    @property
    def listIter(self):
        return self._listIter



if __name__ == "__main__":
    example_string = input("enter string: ")
    int_list = list(map(int, example_string.split(",")))
    listf = bubbleSort(int_list)
    print("Original List")
    print(listf.listO)
    print("Sorted List")
    print(listf.listS)

