class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def out_of_range(i, j):
            return i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1


        def check_rec(board, word, num, i, j):
            if out_of_range(i, j) or board[i][j] != word[num]:
                return False

            if num == len(word) - 1:
                return True

            tmp = board[i][j]
            board[i][j] = '#'

            found = (
                check_rec(board, word, num + 1, i + 1, j) or
                check_rec(board, word, num + 1, i - 1, j) or
                check_rec(board, word, num + 1, i, j + 1) or
                check_rec(board, word, num + 1, i, j - 1)
            )

            board[i][j] = tmp
            return found
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if check_rec(board, word, 0, i, j) == True:
                    return True

        return False