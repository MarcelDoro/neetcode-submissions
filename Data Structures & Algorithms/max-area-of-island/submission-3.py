class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or grid[i][j] == 0:
                return 0

            grid[i][j] = 0

            return 1 + dfs(i + 1, j) + dfs(i, j + 1) + dfs(i - 1, j) + dfs(i, j - 1)
            

        max_area = 0
        for i in range(ROWS):
            for j in range(COLS):
                max_area = max(max_area, dfs(i, j))    

        return max_area