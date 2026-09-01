class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        possible_val = set()

        for n in nums:
            tmp = set()
            for val in possible_val:
                tmp.add(n + val)
            
            possible_val = possible_val | tmp
            possible_val.add(n)

        return sum(nums) / 2 in possible_val
