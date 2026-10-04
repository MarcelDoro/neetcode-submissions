class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def str_to_int(num: str) -> int:
            res = 0
            mul = 1
            for i in range(len(num) - 1, -1, -1):
                res += mul * int(num[i])
                mul *= 10

            return res

        
        def int_to_str(num: int) -> str:
            if num == 0:
                return '0'
                
            res = ''
            while num > 0:                
                digit = chr(48 + num % 10)
                res = digit + res
                num //= 10

            return res

        
        return int_to_str(str_to_int(num1) * str_to_int(num2))
