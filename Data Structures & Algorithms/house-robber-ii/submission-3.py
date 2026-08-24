class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob1(nums: List[int]) -> int:
            r1, r2 = 0, 0            

            for n in nums:
                tmp = max(r1 + n, r2)
                r1 = r2
                r2 = tmp
                
            return r2    

        return max(nums[0], rob1(nums[1:]), rob1(nums[0:-1]))
        