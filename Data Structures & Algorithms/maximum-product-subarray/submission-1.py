class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_max, cur_min = 1, 1

        for num in nums:            
            tmp = cur_max
            cur_max = max(cur_max * num, cur_min * num, num)
            cur_min = min(tmp * num, cur_min * num, num)
            res = max(res, cur_max)
            
        return res
