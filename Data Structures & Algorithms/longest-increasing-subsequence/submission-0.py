class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[len(nums) - 1] = 1

        for i in range(len(nums) - 2, -1, -1):
            curr_max = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    curr_max = max(curr_max, 1 + dp[j])

            dp[i] = curr_max        

        return max(dp)
