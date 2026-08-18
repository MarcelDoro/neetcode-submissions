class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        min_heap = []
        heapq.heapify(min_heap)
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        res = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        heapq.heappush(min_heap, (grid[0][0], 0, 0))
        while min_heap:
            val, r, c = heapq.heappop(min_heap)            
            visited.add((r, c))
            res = max(val, res)
            if (r, c) == (ROWS - 1, COLS - 1):
                return res

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if (0 <= new_r < ROWS and
                    0 <= new_c < COLS and 
                    not (new_r, new_c) in visited):
                    heapq.heappush(min_heap, (grid[new_r][new_c], new_r, new_c))
