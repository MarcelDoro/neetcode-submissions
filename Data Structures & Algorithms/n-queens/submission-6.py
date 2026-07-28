class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        negDiag = set()
        posDiag = set()        

        res = []
        board = [['.' for i in range(n)] for i in range(n)]

        def dfs(r):
            if r >= n:
                res.append([''.join(row) for row in board])
                return

            for c in range(n):
                if not c in cols and not (c - r) in negDiag and not (c + r) in posDiag:
                    board[r][c] = 'Q'
                    cols.add(c)
                    negDiag.add(c - r)
                    posDiag.add(c + r)

                    dfs(r + 1)
                    
                    board[r][c] = '.'
                    cols.remove(c)
                    negDiag.remove(c - r)
                    posDiag.remove(c + r)

        dfs(0)
        return res
