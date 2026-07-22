class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        temp = []
        def dfs():
            if len(temp) >= len(nums):
                res.append(temp.copy())
                return

            for num in nums:
                if not num in temp: 
                    temp.append(num)
                    dfs()
                    temp.pop()

        dfs()
        return res                                        