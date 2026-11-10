class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        count_1 = 0
        count_neighbours = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count_1 += 1
                
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_i = i + di
                    new_j = j + dj
                    if (grid[i][j] == 1 and
                        0 <= new_i < n and 0 <= new_j < m and 
                        grid[new_i][new_j] == 1):
                        count_neighbours += 1
                
        return 4 * count_1 - count_neighbours
