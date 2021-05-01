class bubbleSort:

    def __init__(self, data):
        self.nums = data

    def sort(self, asending):
        if asending:
            for i in range(len(self.nums)-1, 0, -1):
                for j in range(i):
                    if self.nums[j]>self.nums[j+1]:
                        temp = self.nums[j]
                        self.nums[j] = self.nums[j+1]
                        self.nums[j+1] = temp
        else:
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


def listify(num):
    unSortedList = list(map(int, num.split(",")))
    sortedList = bubbleSort(unSortedList)
    sortedList.sort(True)
    sortedList.dump()
    return sortedList.stringify()
