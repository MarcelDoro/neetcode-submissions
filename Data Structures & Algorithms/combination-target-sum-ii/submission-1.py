class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res: list[list[int]] = []

        candidates.sort()
        print(candidates)
        nums: list[int] = []
        curr_sum = 0
        def dfs(i: int) -> None:
            nonlocal curr_sum
            if curr_sum >= target or i >= len(candidates):
                if curr_sum == target:                    
                    res.append(nums.copy())
                return

            nums.append(candidates[i])
            curr_sum += candidates[i]            
            dfs(i + 1)
            nums.pop()
            curr_sum -= candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return res