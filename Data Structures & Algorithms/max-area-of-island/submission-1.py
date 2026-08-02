class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        max_area = 0
        def dfs(i, j):
            nonlocal max_area, area

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            if (
                0 <= i < ROWS and
                0 <= j < COLS and
                grid[i][j] == 1
            ):                
                grid[i][j] = 0
                area += 1

                max_area = max(area, max_area)

                for di, dj in directions:                    
                    dfs(i + di, j + dj)

        for i in range(ROWS):
            for j in range(COLS):
                area = 0
                dfs(i, j)

        return max_area