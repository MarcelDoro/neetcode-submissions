class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for a in range(n):
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            for b in range(a + 1, n):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                l, r = b + 1, n - 1
                while l < r:
                    total = nums[a] + nums[b] + nums[l] + nums[r]

                    if total == target:
                        res.append([nums[a], nums[b], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1

                    elif total > target:
                        r -= 1
                    else:
                        l += 1

        return res
        