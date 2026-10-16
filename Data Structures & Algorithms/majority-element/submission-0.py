class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        min_appears = math.floor(len(nums) / 2)

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            if counter[num] > min_appears:
                return num

        return None
