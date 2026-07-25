class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific = [[False] * COLS for i in range(ROWS)]
        atlantic = [[False] * COLS for i in range(ROWS)]

        def bfs(ocean_side, ocean_end):
            queue = deque(ocean_side)

            def addocean(r, c, row, col):
                if (0 <= r < ROWS and 0 <= c < COLS and
                    not ocean_end[r][c] and heights[row][col] <= heights[r][c]):
                    queue.append([r, c])

            while queue:
                row, col = queue.popleft()
                ocean_end[row][col] = True

                addocean(row + 1, col, row, col)
                addocean(row, col + 1, row, col)
                addocean(row - 1, col, row, col)
                addocean(row, col - 1, row, col)
        
        paci_side = []
        atla_side = []

        for col in range(COLS):
            paci_side.append([0, col])
            atla_side.append([ROWS - 1, col])
        
        for row in range(ROWS):
            paci_side.append([row, 0])
            atla_side.append([row, COLS - 1])
        
        bfs(paci_side, pacific)
        bfs(atla_side, atlantic)

        res = []
        for row in range(ROWS):
            for col in range(COLS):
                if pacific[row][col] and atlantic[row][col]:
                    res.append([row, col])

        return res