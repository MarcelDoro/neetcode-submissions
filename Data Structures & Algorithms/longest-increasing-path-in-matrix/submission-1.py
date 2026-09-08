class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        cache = {}
        def dfs(r: int, c: int, pre: int) -> int:
            if (r, c) in cache:
                return cache[(r, c)]
                
            cache[(r, c)] = 1

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if (0 <= new_r < ROWS and
                    0 <= new_c < COLS and
                    matrix[new_r][new_c] > pre):
                    curr_len = 1 + dfs(new_r, new_c, matrix[new_r][new_c])
                    cache[(r, c)] = max(cache[(r, c)], curr_len)
            
            return cache[(r, c)]


        max_inc_len = 0
        for r in range(ROWS):
            for c in range(COLS):
                max_inc_len = max(max_inc_len, dfs(r, c, matrix[r][c]))

        return max_inc_len
