class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]

        sums = []
        total = 0
        for num in nums:
            total = total + num
            sums.append(total)
            if total < 0:
                total = 0

        return max(sums)
