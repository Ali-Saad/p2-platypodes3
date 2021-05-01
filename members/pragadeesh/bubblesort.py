class bubbleSort:
    def __init__(self, int_list):
        self._listO = []
        self._listO += int_list
        self._listS = int_list
        for i in range(len(self._listS) - 1, 0, -1):  # (6, -1, 0, -1)
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


if __name__ == "__main__":
    string = input("enter string: ")
    int_list = list(map(int, string.split(",")))
    sortedList = bubbleSort(int_list)

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