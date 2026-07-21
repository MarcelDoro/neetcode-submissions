class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        curr_sum = 0
        numbers = []
        def dfs(i):
            nonlocal curr_sum
            if curr_sum >= target or i >= len(nums):
                if curr_sum == target:
                    res.append(numbers.copy())

                return

            numbers.append(nums[i])
            curr_sum += nums[i]
            dfs(i)
            numbers.pop()
            curr_sum -= nums[i]
            dfs(i + 1)

        dfs(0)
        return res
