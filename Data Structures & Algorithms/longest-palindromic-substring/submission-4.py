class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(s: str) -> bool:
            l, r = 0, len(s) - 1

            while l < r:
                if s[l] != s[r]:
                    return False
                
                l += 1
                r -= 1

            return True

        res = ''

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r + 1]

                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r + 1]

                l -= 1
                r += 1

        return res
