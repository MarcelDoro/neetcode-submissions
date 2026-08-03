class Solution:
    def hammingWeight(self, n: int) -> int:
        def dec_to_bin(n: int) -> int:
            binary = ''

            while n > 0:
                binary = str(n % 2) + binary
                n //= 2
                
            if binary == '':
                return 0
            else:
                return int(binary)


        n = dec_to_bin(n)
        counter = 0
        
        while n > 0:
            counter += n % 10
            n //= 10
            
        return counter