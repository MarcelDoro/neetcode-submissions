class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
       i = 1
       while True:
        if not i in nums:
            return i

        i += 1
