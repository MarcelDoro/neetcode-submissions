class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            missing = target - numbers[i]
            l = 0
            r = n - 1
            m = (l + r) // 2
            while l != r:
                if numbers[m] > missing:
                    r = m - 1
                else:
                    l = m
                m = (l + r) // 2 + 1
                
            if numbers[i] + numbers[r] == target:
                return [i + 1, r + 1]



