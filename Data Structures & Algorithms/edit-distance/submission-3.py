class Solution:
    def minDistance(self, word1: str, word2: str) -> int:   
        n, m = len(word1), len(word2)     
        cache = {} #key: (i, j), val: min_of_operations
        def dfs(i: int, j: int) -> int:
            if i >= n and j >= m:
                return 0
            
            if (i, j) in cache:
                return cache[(i, j)]

            if i >= n:
                cache[(i, j)] = 1 + dfs(i, j + 1) # insert
                return cache[(i, j)] 
            if j >= m:
                cache[(i, j)] = 1 + dfs(i + 1, j) # delete
                return cache[(i, j)]

            if word1[i] == word2[j]:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            
            insert = 1 + dfs(i, j + 1)
            delete = 1 + dfs(i + 1, j)
            replace = 1 + dfs(i + 1, j + 1)

            cache[(i, j)] = min(insert, delete, replace)
            return cache[(i, j)]


        return dfs(0, 0)
