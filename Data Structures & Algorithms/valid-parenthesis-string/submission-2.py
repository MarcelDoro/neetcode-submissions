class Solution:
    def checkValidString(self, s: str) -> bool:
        cache = {}
        def dfs(i: int, count_open: int) -> bool:
            if i == len(s):
                return count_open == 0
            if (i, count_open) in cache:
                return cache[(i, count_open)]

            if count_open < 0:
                cache[(i, count_open)] = False
                return cache[(i, count_open)]

            if s[i] == '(':
                cache[(i, count_open)] = dfs(i + 1, count_open + 1)
                return cache[(i, count_open)]
            if s[i] == ')':
                cache[(i, count_open)] = dfs(i + 1, count_open - 1)
                return cache[(i, count_open)]
            if s[i] == '*':
                cache[(i, count_open)] = (dfs(i + 1, count_open + 1) or
                                        dfs(i + 1, count_open - 1) or
                                        dfs(i + 1, count_open))
                return cache[(i, count_open)]
                
        
        return dfs(0, 0)
