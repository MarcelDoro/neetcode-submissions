class Solution:
    def countBits(self, n: int) -> List[int]:
        def int_to_bin(n: int) -> str:
            if n == 0:
                return '0'

            res = ""
            while n > 0:
                dig = str(n % 2)
                res = dig + res
                n //= 2

            return res

        return [int_to_bin(i).count('1') for i in range(n + 1)]
