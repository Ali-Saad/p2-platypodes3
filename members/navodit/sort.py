class bubbleSort:

    def __init__(self, data):
        self.nums = data

    def sort(self, select):
        if select == "1":
            for i in range(len(self.nums)-1, 0, -1):
                for j in range(i):
                    if self.nums[j]>self.nums[j+1]:
                        temp = self.nums[j]
                        self.nums[j] = self.nums[j+1]
                        self.nums[j+1] = temp
        if select == "2":
            for i in range(len(self.nums)-1, 0, -1):
                for j in range(i):
                    if self.nums[j]<self.nums[j+1]:
                        temp = self.nums[j]
                        self.nums[j] = self.nums[j+1]
                        self.nums[j+1] = temp


    def dump(self):
        print(self.nums)

    def getList(self):
        return self.nums

    def stringify(self):
        output = [str(x) for x in self.nums]
        return output


def listify(num, select):
    print(num,select)
    unSortedList = list(map(int, num.split(",")))
    sortedList = bubbleSort(unSortedList)
    sortedList.sort(select)
    sortedList.dump()
    return sortedList.stringify()
