class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for key, val in counter.items():
            if val == 1:
                return key

        return -1
        