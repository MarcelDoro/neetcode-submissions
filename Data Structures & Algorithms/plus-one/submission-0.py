class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        mul = 1
        for i in range(len(digits) - 1, -1, -1):
            number += mul * digits[i]
            mul *= 10

        number += 1

        reversed_res = []
        while number > 0:
            reversed_res.append(number % 10)
            number //= 10

        reversed_res.reverse()
        return reversed_res
