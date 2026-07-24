class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        dist = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visit.add((r, c))
        
        def addcell(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                (r, c) in visit or grid[r][c] == -1):
                return
            queue.append((r, c))
            visit.add((r, c))

        while queue:
            for level in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist

                addcell(r + 1, c)
                addcell(r, c + 1)
                addcell(r - 1, c)
                addcell(r, c -1)
            dist += 1