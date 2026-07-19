class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        l = 0
        r = len(self.nums)

        while l < r:
            m = (l + r) // 2
            if self.nums[m] < num:
                l = m + 1
            else:
                r = m

        self.nums.insert(l, num)

    def findMedian(self) -> float:
        if len(self.nums) % 2 == 0:
            a, b = self.nums[len(self.nums) // 2 - 1], self.nums[len(self.nums) // 2]
            return (a + b) / 2
        else:
            return self.nums[len(self.nums) // 2]
        