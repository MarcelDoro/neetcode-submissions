class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def no_queen_can_attack(board):
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 'Q':
                        # Check horizontally                        
                        for m in range(n):
                            if (i, j) != (i, m) and board[i][m] == 'Q':
                                return False
                        
                        # Check vertically                        
                        for m in range(n):
                            if (i, j) != (m, j) and board[m][j] == 'Q':
                                return False

                        # Check diagonally
                        a, b = i - 1, j - 1
                        while a >= 0 and b >= 0:
                            if board[a][b] == 'Q':
                                return False
                            
                            a -= 1
                            b -= 1
                        
                        a, b = i + 1, j + 1
                        while a < n and b < n:
                            if board[a][b] == 'Q':
                                return False

                            a += 1
                            b += 1

                        a, b = i - 1, j + 1
                        while a >= 0 and b < n:
                            if board[a][b] == 'Q':
                                return False

                            a -= 1
                            b += 1
                        
                        a, b = i + 1, j - 1
                        while a < n and b >= 0:
                            if board[a][b] == 'Q':
                                return False

                            a += 1
                            b -= 1
            
            return True


        res = []
        tmp = [['.' for i in range(n)] for i in range(n)]

        def dfs(r):
            if r == n:
                res.append([''.join(row) for row in tmp])
                return 

            for c in range(n):
                tmp[r][c] = 'Q'                                        
                
                if no_queen_can_attack(tmp):
                    dfs(r + 1)

                tmp[r][c] = '.'
                
        dfs(0)        

        return res
