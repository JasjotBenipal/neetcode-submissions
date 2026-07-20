class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() # r + c
        negDiag = set() # r - c

        res = []
        
        board = [["."] * n for i in range(n)]

        def backtrack(row):
            if row == n:
                res.append(["".join(row) for row in board])
                return
            
            for column in range(n):
                if column in col or (row + column) in posDiag or (row - column) in negDiag:
                    continue

                col.add(column) 
                posDiag.add(row + column)
                negDiag.add(row - column)
                board[row][column] = "Q"

                backtrack(row + 1)

                col.remove(column) 
                posDiag.remove(row + column)
                negDiag.remove(row - column)
                board[row][column] = "."
        
        backtrack(0)
        return res