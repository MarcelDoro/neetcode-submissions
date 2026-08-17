class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def man_distance(start: List[int], end: List[int]):
            return abs(start[0] - end[0]) + abs(start[1] - end[1])


        n = len(points)
        adj = { i:[] for i in range(n) }

        for i in range(n):
            for j in range(i + 1, n):
                dis = man_distance(points[i], points[j])
                adj[i].append((dis, j))
                adj[j].append((dis, i))
        
        res = 0
        visited = set()
        frontier = []
        heapq.heapify(frontier)
        visited.add(0)
        for pair in adj[0]:
            heapq.heappush(frontier, pair)

        while len(visited) != n:
            dis, node = heapq.heappop(frontier)
            if node in visited:
                continue

            res += dis
            visited.add(node)
            for pair in adj[node]:
                heapq.heappush(frontier, pair)
            
        return res
