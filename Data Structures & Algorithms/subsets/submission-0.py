class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                subsets.append(subset.copy())
                return

            dfs(i + 1)
            subset.append(nums[i])
            dfs(i + 1)
            subset.remove(nums[i])

        dfs(0)
        return subsets
            