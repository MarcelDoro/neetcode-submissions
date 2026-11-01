class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        guess = 1
        while True:
            if not guess in counter:
                return guess
            guess += 1

        return guess