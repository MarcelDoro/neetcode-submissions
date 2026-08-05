from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]        

        def bfs(start_i, start_j):
            q = deque([(start_i, start_j, 0)])
            visited = {(start_i, start_j)}

            while q:
                i, j, dis = q.popleft()
                grid[i][j] = min(grid[i][j], dis)

                for di, dj in directions:
                    new_i, new_j = i + di, j + dj
                    if (0 <= new_i < ROWS and
                        0 <= new_j < COLS and
                        grid[new_i][new_j] != -1 and
                        not (new_i, new_j) in visited):

                        q.append((new_i, new_j, dis + 1))
                        visited.add((new_i, new_j))
            

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:                    
                    bfs(i, j)
