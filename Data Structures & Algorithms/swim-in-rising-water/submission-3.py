class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        min_heap = [(grid[0][0], 0, 0)]        
        N = len(grid)
        visited = set()
        res = 0
       
        while min_heap:
            val, r, c = heapq.heappop(min_heap)            
            visited.add((r, c))
            res = max(val, res)
            if (r, c) == (N - 1, N - 1):
                return res

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r, new_c = r + dr, c + dc
                if (0 <= new_r < N and
                    0 <= new_c < N and 
                    not (new_r, new_c) in visited):
                    heapq.heappush(min_heap, (grid[new_r][new_c], new_r, new_c))
