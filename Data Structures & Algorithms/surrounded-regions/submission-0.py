class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        queue = deque()

        for row in range(ROWS):
            if board[row][0] == "O":
                queue.append([row, 0])
            if board[row][COLS - 1] == "O":
                queue.append([row, COLS - 1])
        
        for col in range(COLS):
            if board[0][col] == "O":
                queue.append([0, col])
            if board[ROWS - 1][col] == "O":
                queue.append([ROWS - 1, col])

        cover = [[False] * COLS for i in range(ROWS)]

        def addo(r, c):
            if (0 <= r < ROWS and 0 <= c < COLS and not cover[r][c] and
                board[r][c] == "O"):
                queue.append([r, c])

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                cover[r][c] = True
                addo(r + 1, c)
                addo(r, c + 1)
                addo(r - 1, c)
                addo(r, c - 1)
        
        for row in range(ROWS):
            for col in range(COLS):
                if not cover[row][col]:
                    board[row][col] = "X"
