class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = {}

        def dfs(i: int) -> bool:
            if i in cache:
                return cache[i]
            
            if i >= len(nums) - 1:
                cache[i] = True
                return cache[i]
            
            if nums[i] == 0:
                cache[i] = False
                return cache[i]

            exist_path = False
            for jump in range(nums[i], 0, -1):
                exist_path = exist_path or dfs(i + jump)

            cache[i] = exist_path
            return cache[i]

        return dfs(0)
