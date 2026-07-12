class Trie:
    def __init__(self):
        self.children = {}
        self.endWord = False

    def insert(self, words):
        for word in words:
            cur = self
            for char in word:
                if char not in cur.children:
                    cur.children[char] = Trie()
                cur = cur.children[char]
            cur.endWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        root.insert(words)
        
        ROWS, COLS = len(board) - 1, len(board[0]) - 1

        res, visit = set(), set()
        
        def dfs(row, col, trieNode, WordSoFar):
            if (row < 0 or row > ROWS or col < 0 or col > COLS or 
                (row, col) in visit or board[row][col] not in trieNode.children):
                return
            
            visit.add((row, col))
            WordSoFar += board[row][col]
            trieNode = trieNode.children[board[row][col]]

            if trieNode.endWord:
                res.add(WordSoFar)
            
            dfs(row + 1, col, trieNode, WordSoFar)
            dfs(row, col + 1, trieNode, WordSoFar)
            dfs(row - 1, col, trieNode, WordSoFar)
            dfs(row, col - 1, trieNode, WordSoFar)
            visit.remove((row, col))
        
        for rows in range(ROWS + 1):
            for cols in range(COLS + 1):
                dfs(rows, cols, root, "")
        
        return list(res)