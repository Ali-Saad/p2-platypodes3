class alibubbleSort:
    def __init__(self, data):
        # initing the arugmnet
        self.nums = data

        self.sort(self.nums)

    def sort(self, select):
        for i in range(len(self.nums)-1, 0, -1):
            for j in range(i):
                if self.nums[j]>self.nums[j+1]:
                    temp = self.nums[j]
                    self.nums[j] = self.nums[j+1]
                    self.nums[j+1] = temp
    @property
    def print(self):
        print(self.nums)
    @property
    def grab(self):
        return self.nums
    @property
    def string(self):
        return self.nums


if __name__=="__main__":
    unSortedList = [1000,10,1234,12341, 12341, 12341234]
    sortedList = alibubbleSort(unSortedList)
    print(sortedList.string)