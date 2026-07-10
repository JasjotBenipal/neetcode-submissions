class PrefixTree:

    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def insert(self, word: str) -> None:
        cur = self

        for char in word:
            if char not in cur.children:
                cur.children[char] = PrefixTree()
            cur = cur.children[char]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self

        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self

        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True
        