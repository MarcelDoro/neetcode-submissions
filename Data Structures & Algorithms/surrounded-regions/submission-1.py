class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        do_not_change = set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def add_to_unchanged(r: int, c: int, unchanged: set()) -> None:
            if board[r][c] == 'X':
                return 

            if board[r][c] == 'O' and (r, c) not in unchanged:
                unchanged.add((r, c))

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc

                if (0 <= new_r < ROWS and
                    0 <= new_c < COLS and
                    board[new_r][new_c] == 'O' and
                    (new_r, new_c) not in unchanged):

                    add_to_unchanged(new_r, new_c, unchanged)


        for r in range(ROWS):
            add_to_unchanged(r, 0, do_not_change)
            add_to_unchanged(r, COLS - 1, do_not_change)
            print(r)
            print(do_not_change)

        

        for c in range(COLS):
            add_to_unchanged(0, c, do_not_change)
            add_to_unchanged(ROWS - 1, c, do_not_change)

        

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r, c) not in do_not_change:
                    board[r][c] = 'X'
