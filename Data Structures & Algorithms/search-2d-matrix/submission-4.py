class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        
        l = 0
        r = m * n - 1
        mid = (l + r) // 2

        while l <= r:
            if target == matrix[mid // m][mid % m]:
                return True
            if l == r:
                return target == matrix[mid // m][mid % m]
            elif matrix[mid // m][mid % m] < target:
                l = mid + 1
            else:
                r = mid - 1

            mid = (l + r) // 2
           
        return target == matrix[mid // m][mid % m]