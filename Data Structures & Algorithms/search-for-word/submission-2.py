class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.res = False
        checked = set()
        ROW, COL = len(board), len(board[0])

        def dfs(x, y, i):
            if (x < 0 or y < 0 or x >= ROW or y >= COL or 
                (x, y) in checked or i == len(word) or word[i] != board[x][y]):
                return

            # add current char to substring as we going deeper
            checked.add((x, y))

            if i + 1 == len(word):
                self.res = True

            dfs(x - 1, y, i + 1)
            dfs(x + 1, y, i + 1)
            dfs(x, y + 1, i + 1)
            dfs(x, y - 1, i + 1)
            
            # remove current char as we return to prev char
            checked.remove((x, y))
        
        #call dfs to run here
        for x in range(len(board)):
            for y in range(len(board[0])):
                dfs(x, y, 0)
        return self.res