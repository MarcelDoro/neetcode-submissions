class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        i = 1
        while True:
            if not i in nums_set:
                return i

            i += 1
