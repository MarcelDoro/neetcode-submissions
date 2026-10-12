class Solution:
    def reverse(self, x: int) -> int:
        positive = True if x >= 0 else False
        x = -x if x < 0 else x
        n = 0
        tmp = x
        while tmp > 0:
            tmp //= 10
            n += 1       
    
        res = 0
        power = pow(10, n - 1)
        while x > 0:
            res += power * (x % 10)
            power //= 10
            x //= 10
                
        res = res if positive else -res
        if pow(-2, 31) <= res <= pow(2, 31) - 1:
            return res
        else:
            return 0
            