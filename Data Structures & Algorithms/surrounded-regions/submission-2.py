class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        do_not_change = set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def add_to_unchanged(r: int, c: int, unchanged: set()) -> None:
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                board[r][c] == 'X' or
                (r, c) in unchanged):

                return 

            if board[r][c] == 'O' and (r, c) not in unchanged:
                unchanged.add((r, c))

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                add_to_unchanged(new_r, new_c, unchanged)


        for r in range(ROWS):
            add_to_unchanged(r, 0, do_not_change)
            add_to_unchanged(r, COLS - 1, do_not_change)

        for c in range(COLS):
            add_to_unchanged(0, c, do_not_change)
            add_to_unchanged(ROWS - 1, c, do_not_change)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r, c) not in do_not_change:
                    board[r][c] = 'X'
