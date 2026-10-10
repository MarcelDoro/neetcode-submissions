class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set_nums = set()
        for num in nums:
            set_nums.add(num)

        max_n = max(nums)
        for n in range(max_n):
            if not n in set_nums:
                return n

        return max_n + 1