class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])

        def process_an_island(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or grid[i][j] == '0':
                return 

            grid[i][j] = '0'

            for di, dj in directions:
                process_an_island(i + di, j + dj)


        num_of_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    num_of_islands += 1
                    process_an_island(i, j)
        
        return num_of_islands
