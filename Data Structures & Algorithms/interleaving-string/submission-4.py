class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        def dfs(i: int, j: int) -> bool:
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in memo:
                return memo[(i, j)]
            
            k = i + j
            if i < len(s1) and s1[i] == s3[k]:
                memo[(i, j)] = dfs(i + 1, j)                
            
            if j < len(s2) and s2[j] == s3[k]:
                memo[(i, j)] = dfs(i, j + 1)                    
            
            if not (i, j) in memo:
                memo[(i, j)] = False
                
            return memo[(i, j)]

        
        return False if len(s1) + len(s2) != len(s3) else dfs(0, 0)
