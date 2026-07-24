class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        self.fresh = 0
        count = 0
        queue = deque()
        visit = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visit.add((r, c))
                elif grid[r][c] == 1:
                    self.fresh += 1
        
        def addfruit(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or
                (r, c) in visit or grid[r][c] == 0):
                return
            
            self.fresh -= 1
            visit.add((r, c))
            queue.append((r, c))

        while queue and self.fresh:
            for level in range(len(queue)):
                r, c = queue.popleft()

                addfruit(r + 1, c)
                addfruit(r, c + 1)
                addfruit(r - 1, c)
                addfruit(r, c - 1)
            
            count += 1
        
        return count if not self.fresh else -1