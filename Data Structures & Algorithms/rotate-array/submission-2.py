class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            new_i = (i + k) % len(nums)
            res[new_i] = nums[i]

        nums[:] = res
