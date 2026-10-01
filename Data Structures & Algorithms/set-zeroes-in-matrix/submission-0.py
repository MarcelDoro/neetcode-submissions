class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        zeros_indexes = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zeros_indexes.add((i, j))

        for i in range(n):
            for j in range(m):
                if (i, j) in zeros_indexes:
                    # Set 0 in a column
                    for k in range(n):
                        matrix[k][j] = 0

                    # Set 0 in a row
                    for k in range(m):
                        matrix[i][k] = 0
        