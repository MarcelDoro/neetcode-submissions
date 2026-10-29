class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = 0
        end = k - 1
        n = len(nums)
        res = []


        while end < n:
            maxi = nums[start]
            for i in range(start + 1, end + 1):
                if nums[i] > maxi:
                    maxi = nums[i]
            res.append(maxi)
            start += 1
            end += 1

        return res