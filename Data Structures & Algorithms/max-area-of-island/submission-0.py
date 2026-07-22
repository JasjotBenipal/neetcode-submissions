class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0

        ROWS, COLS = len(grid), len(grid[0])

        counted = set()

        def dfs(row, col):
            if (row < 0 or col < 0 or row >= ROWS or col >= COLS or
                (row, col) in counted or grid[row][col] == 0):
                return 0
            
            counted.add((row, col))

            return (1 + dfs(row + 1, col) + 
                    dfs(row, col + 1) +
                    dfs(row - 1, col) +
                    dfs(row, col - 1))

        for row in range(ROWS):
            for col in range(COLS):
                res = max(res, dfs(row, col))
        
        return res