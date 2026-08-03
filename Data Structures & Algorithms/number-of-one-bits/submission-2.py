class Solution:
    def hammingWeight(self, n: int) -> int:
        def dec_to_bin(n: int) -> int:
            binary = ''

            while n > 0:
                binary = str(n % 2) + binary
                n //= 2
                
            return 0 if binary == '' else int(binary)


        n = dec_to_bin(n)
        counter = 0
        
        while n > 0:
            counter += n % 10
            n //= 10
            
        return counter