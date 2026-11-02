class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        original_len = len(nums)
        deleted = 0
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                del nums[i + 1]
                deleted += 1
            else:                
                i += 1

        return original_len - deleted
