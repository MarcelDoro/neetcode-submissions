class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        possible_sums = set()
        target = total_sum / 2
        for n in nums:
            tmp = set()
            for pre_sum in possible_sums:
                new_sum = n + pre_sum
                if new_sum == target:
                    return True
                tmp.add(new_sum)
            possible_sums = possible_sums | tmp
            possible_sums.add(n)

        return target in possible_sums
