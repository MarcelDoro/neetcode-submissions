class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = {}

        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                return n
