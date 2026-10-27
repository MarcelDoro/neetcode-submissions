class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        min_appearance = math.floor(len(nums) / 3)
        res = []
        for key in count:
            if count[key] > min_appearance:
                res.append(key)

        return res
