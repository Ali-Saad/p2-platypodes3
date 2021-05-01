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
    # string = input("enter string: ")
    string = "43,7,9,2"
    sortedList = bubbleSort(string)

    print("Original List")
    print(sortedList.listO)

    print("Sorted list")
    print(sortedList.listS)


'''list_to_sort = [8, 5, 2, 6, 1, 5, 7]
listO = []
print('Original List: ', list_to_sort)
listO.append(int_list)
print("OriginalList")
print(listO)

bubbleSort.__init__(int_list)
listS = []
listS.append(int_list)
print("Sorted List")
print(listS)
print('Sorted List: ', list_to_sort)'''