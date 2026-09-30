class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        upper_row, lower_row = 0, n
        left_col, right_col = 0, m

        x, y = 0, 0
        res = []
        while True:
            res.append(matrix[x][y])

            # Move right
            while y < right_col - 1:
                y += 1
                res.append(matrix[x][y])            
            upper_row += 1
            if len(res) >= n * m:
                break
            
            # Move down
            while x < lower_row - 1:
                x += 1
                res.append(matrix[x][y])            
            right_col -= 1
            if len(res) >= n * m:
                break

            # Move left
            while y > left_col:
                y -= 1
                res.append(matrix[x][y])
            lower_row -= 1
            if len(res) >= n * m:
                break

            # Move up
            while x > upper_row:
                x -= 1
                res.append(matrix[x][y])
            left_col += 1
            if len(res) >= n * m:
                break

            y += 1

        return res
    