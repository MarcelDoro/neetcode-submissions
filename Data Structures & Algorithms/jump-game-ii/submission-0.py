class Solution:
    def jump(self, nums: List[int]) -> int:
        min_jumps = [ float('inf') for _ in range(len(nums)) ]
        min_jumps[0] = 0

        for i in range(len(nums)):            
            for j in range(i + 1, i + nums[i] + 1):
                if j < len(nums):
                    min_jumps[j] = min(min_jumps[j], min_jumps[i] + 1)

        return min_jumps[-1]
