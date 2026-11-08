class Solution:
    def validPalindrome(self, s: str) -> bool:        
        def is_palindrome(s: str) -> bool:
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                
                l += 1
                r -= 1

            return True

        if is_palindrome(s):
            return True

        for i in range(len(s)):                    
            if is_palindrome(s[0:i] + s[i + 1:len(s)]):
                return True            

        return False
