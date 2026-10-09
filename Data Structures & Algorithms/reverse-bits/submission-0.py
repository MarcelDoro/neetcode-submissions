class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        mul = 2**31
        while n > 0:
            dig = n % 2
            res += dig * mul
            n //= 2
            mul //= 2

        return res
