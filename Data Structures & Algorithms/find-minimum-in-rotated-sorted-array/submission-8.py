class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        mini = nums[0]
        
        while r - l > 1:
            if nums[l] < nums[r]:
                return nums[l]
            m = (l + r) // 2       
            print(l, r, m)   
            if nums[m] >= nums[l]:
                l = m
            else:
                r = m

        return min(nums[l], nums[r])