class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1 or n == 0:
            return 1

        if x == -1:
            return 1 if n % 2 == 0 else -1
        
        cache = {}
        def power(x: float, n: int) -> float:
            if (x, n) in cache:
                return cache[(x, n)]

            if n == 1:
                return x

            if n % 2 != 0:
                cache[(x, n)] = power(x, n // 2) * power(x, n // 2 + 1)              
            else:
                cache[(x, n)] = power(x, n // 2) * power(x, n // 2)

            return cache[(x, n)]
            
        return power(x, n) if n >= 0 else 1 / power(x, -n)