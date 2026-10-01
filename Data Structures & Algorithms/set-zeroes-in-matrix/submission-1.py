class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    # mark column's values to change
                    for k in range(n):
                        if matrix[k][j] != 0:
                            matrix[k][j] = 'x'

                    # mark row's values to change
                    for k in range(m):
                        if matrix[i][k] != 0:
                            matrix[i][k] = 'x'

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 'x':
                    matrix[i][j] = 0
                    