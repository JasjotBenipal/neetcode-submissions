class WordDictionary:

    def __init__(self):
        self.children = {}
        self.word = False

    def addWord(self, word: str) -> None:
        cur = self

        for char in word:
            if char not in cur.children:
                cur.children[char] = WordDictionary()
            cur = cur.children[char]
        cur.word = True

    def search(self, word: str) -> bool:
        cur = self

        def dfs(cur, word):
            for index in range(len(word)):
                if word[index] == ".":
                    for child in cur.children.values():
                        if dfs(child, word[index + 1:]):
                            return True
                    return False
                if word[index] not in cur.children:
                    return False
                cur = cur.children[word[index]]
            return cur.word
        return dfs(cur, word) 