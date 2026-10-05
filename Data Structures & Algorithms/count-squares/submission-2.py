class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        self.points[point] = self.points.get(point, 0) + 1

    def count(self, point: List[int]) -> int:
        point = tuple(point)
        res = 0
        qx, qy = point[0], point[1]
        for list_point in self.points:
            x, y = list_point[0], list_point[1]
            if abs(qx - x) == abs(qy - y) and abs(qx - x) > 0:
                res += (self.points[list_point] * 
                self.points.get((qx, y), 0) *
                self.points.get((x, qy), 0))

        return res
