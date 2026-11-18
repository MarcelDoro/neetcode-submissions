class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        positions = defaultdict(list)
        for i in range(len(nums)):
            positions[nums[i]].append(i)

        for values in positions.values():
            for i, val in enumerate(values):
                values[i] = (val + k) % len(nums)

        for key in positions:
            for position in positions[key]:
                nums[position] = key
        