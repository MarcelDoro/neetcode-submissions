class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob1(nums: List[int]) -> int:
            r1, r2 = 0, 0            

            for n in nums:
                tmp = max(r1 + n, r2)
                r1 = r2
                r2 = tmp
                
            return r2

        if len(nums) == 1:
            return nums[0]
            
        return max(rob1(nums[1:]), rob1(nums[0:len(nums) - 1]))