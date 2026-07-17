class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.res = False
        checked = set()
        ROW, COL = len(board), len(board[0])

        def dfs(x, y, substr):
            if x < 0 or y < 0 or x >= ROW or y >= COL or len(substr) > len(word) or (x, y) in checked:
                return

            # add current char to substring as we going deeper
            substr += board[x][y]
            checked.add((x, y))

            if substr == word:
                self.res = True

            dfs(x - 1, y, substr)
            dfs(x + 1, y, substr)
            dfs(x, y + 1, substr)
            dfs(x, y - 1, substr)
            
            # remove current char as we return to prev char
            substr = substr[:-1]
            checked.remove((x, y))
        
        #call dfs to run here
        for x in range(len(board)):
            for y in range(len(board[0])):
                dfs(x, y, "")
        return self.res