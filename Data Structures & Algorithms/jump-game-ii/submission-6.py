class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        steps = 0

        while r < len(nums) - 1:
            furthest = l
            for i in range(l, r + 1):
                furthest = max(furthest, i + nums[i])

            steps += 1
            l = r + 1
            r = furthest

        return steps    
