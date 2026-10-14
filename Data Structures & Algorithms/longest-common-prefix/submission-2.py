class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        i = 0
        res = ''
        for c in strs[i]:
            for s in strs:
                if i >= len(s) or s[i] != c:
                    return res

            i += 1
            res += c

        return res
