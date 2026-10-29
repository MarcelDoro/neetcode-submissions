class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxi = nums[0]
        n = len(nums)
        res = []

        for i in range(k):
            if nums[i] > maxi:
                maxi = nums[i]
        res.append(maxi)

        for i in range(k, n):
            if nums[i] > maxi:
                maxi = nums[i]
            elif nums[i - k] == maxi:
                maxi = nums[i - k + 1]
                for j in range(i - k + 1, i + 1):
                    if nums[j] > maxi:
                        maxi = nums[j]
            
            res.append(maxi)

        return res
            
