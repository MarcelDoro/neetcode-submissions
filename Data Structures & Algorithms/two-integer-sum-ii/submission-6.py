class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        add = 0
        for i in range(n):
            for j in range(n):
                if i != j and numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]

        return [0, 0]


        