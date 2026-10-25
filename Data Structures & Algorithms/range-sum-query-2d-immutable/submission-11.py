class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        
        self.sum_matrix = [[0 for _ in range(COLS + 1)] for _ in range(ROWS + 1)]
        self.sum_matrix[1][1] = matrix[0][0]        

        for r in range(2, ROWS + 1):
            self.sum_matrix[r][1] = self.sum_matrix[r - 1][1] + matrix[r - 1][0]        
        
        for c in range(2, COLS + 1):           
            self.sum_matrix[1][c] = self.sum_matrix[1][c - 1] + matrix[0][c - 1]        
        
        for r in range(2, ROWS + 1):
            for c in range(2, COLS + 1):
                self.sum_matrix[r][c] = (self.sum_matrix[r][c - 1] +
                self.sum_matrix[r - 1][c] -
                self.sum_matrix[r - 1][c - 1] +
                matrix[r - 1][c - 1])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        
        return (self.sum_matrix[row2][col2] - 
               self.sum_matrix[row1 - 1][col2] - 
               self.sum_matrix[row2][col1 - 1] +
               self.sum_matrix[row1 - 1][col1 - 1])

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)