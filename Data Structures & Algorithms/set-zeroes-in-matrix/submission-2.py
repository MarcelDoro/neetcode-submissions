class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        rows, cols = set(), set()

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for row in rows:
            for k in range(m):
                matrix[row][k] = 0

        for col in cols:
            for k in range(n):
                matrix[k][col] = 0
