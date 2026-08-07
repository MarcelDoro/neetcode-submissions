class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        pacyfic, atlantic = set(), set()

        def dfs(r: int, c: int, visit: set, prev_height: int) -> None:
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visit or
                heights[r][c] < prev_height
            ):
                return

            visit.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pacyfic, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pacyfic, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

        return [[r, c] for r, c in (pacyfic & atlantic)]