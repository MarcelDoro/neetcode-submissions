class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
            
        if len(s) == len(t):
            chars_s = {}
            chars_t = {}
            for c in s:
                if c not in chars_s:
                    chars_s[c] = 1
                else:
                    chars_s[c] += 1

            for c in t:
                if c not in chars_t:
                    chars_t[c] = 1
                else:
                    chars_t[c] += 1
            
            if chars_s == chars_t:
                return s
            else:
                return ""

        chars = {}
        for c in t:
            if c not in chars:
                chars[c] = 1
            else:
                chars[c] += 1

        min_res = s
        exist = False

        for i in range(len(s)):
            string = ""
            chars_s = {}

            for j in range(i, len(s)):
                string += s[j]
                if s[j] not in chars_s:
                    chars_s[s[j]] = 1
                else:
                    chars_s[s[j]] += 1

                is_valid = True
                for k in chars.keys():                    
                    if k not in chars_s:
                        is_valid = False
                        break
                    elif chars_s[k] < chars[k]:
                        is_valid = False
                        break
                    
                if len(string) <= len(min_res) and is_valid == True:
                    exist = True
                    min_res = string
        
        if exist:
            return min_res
        else:
            return ""
