class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_n = max(nums)

        for n in range(max_n):
            if not n in nums:
                return n

        return max(nums) + 1
