class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        min_heap = [(0, 0)] # cost, node
        heapq.heapify(min_heap)
        res = 0

        while len(visited) < n:
            dis, node = heapq.heappop(min_heap)
            if node in visited:
                continue

            res += dis
            visited.add(node)

            x1, y1 = points[node]
            for v in range(n):
                if not v in visited:
                    x2, y2 = points[v]
                    dis = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(min_heap, (dis, v))
            
        return res
