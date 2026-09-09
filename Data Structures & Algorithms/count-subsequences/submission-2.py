class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        def dfs(i: int, word: str) -> int:
            if (i, word) in cache:
                return cache[(i, word)]

            if i >= len(s):
                if word == t:
                    return 1

                return 0

            cache[(i, word)] = dfs(i + 1, word + s[i]) + dfs(i + 1, word)
            return cache[(i, word)]

        return dfs(0, '')
