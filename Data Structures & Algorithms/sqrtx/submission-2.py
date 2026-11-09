class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 0:
            return 0
        if x == 1:
            return 1

        i = 0
        while i <= x:
            if i * i > x:
                return i - 1

            i += 1

        return i
