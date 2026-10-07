class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_1_in_bin(n: int) -> str:
            if n == 0:
                return 0

            res = 0
            while n > 0:
                if n % 2 == 1:
                    res += 1
                n //= 2

            return res

        return [count_1_in_bin(i) for i in range(n + 1)]
