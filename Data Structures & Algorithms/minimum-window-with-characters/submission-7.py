class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "":
            return ""

        count_t = {}
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        m_have = 0
        m_need = len(count_t) #size? Propably count duplicates
        res = ""
        res_len = float("infinity")
        count_s = {}
        count_s[s[0]] = 1
        if s[0] in count_t and count_s[s[0]] == count_t[s[0]]:
            m_have = 1
        start, end = 0, 0 #start and end "pointers"
        while end < len(s) and start <= end:
            if end == 12:
                print("s map:", count_s)
                print("matches have:", m_have)           
            if m_have == m_need:
                print("start, end:", start, end)               
                count_s[s[start]] -= 1
                if m_have == m_need and end - start + 1 < res_len:
                    print("s[start], s[end]:", s[start], s[end]) 
                    res = s[start:end+1]
                    res_len = end - start + 1
                if s[start] in count_t and count_s[s[start]] < count_t[s[start]]:
                    m_have -= 1               
                start += 1
            else:
                end += 1
                if end >= len(s):
                    break
                count_s[s[end]] = 1 + count_s.get(s[end], 0)
                if s[end] in count_t and count_s[s[end]] == count_t[s[end]]:
                    m_have += 1
            
        return res