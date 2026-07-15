class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            points[i].insert(0, points[i][0] ** 2 + points[i][1] ** 2)

        heapq.heapify(points)

        results = []
        for i in range(k):
            dis, x, y = heapq.heappop(points)
            results.append([x, y])

        return results