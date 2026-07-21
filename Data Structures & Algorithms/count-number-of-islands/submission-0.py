class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.res = 0
        foundSoFar = set()

        ROW, COL = len(grid), len(grid[0])

        def dfs(row, col, n):
            if (row < 0 or col < 0 or row >= ROW or col >= COL or 
                (row, col) in foundSoFar or grid[row][col] == "0"):
                return
            
            foundSoFar.add((row, col))

            dfs(row + 1, col, n + 1)
            dfs(row - 1, col, n + 1)
            dfs(row, col + 1, n + 1)
            dfs(row, col - 1, n + 1)

            if n == 0:
                self.res += 1
        
        for rows in range(ROW):
            for cols in range(COL):
                dfs(rows, cols, 0)
        
        return self.res