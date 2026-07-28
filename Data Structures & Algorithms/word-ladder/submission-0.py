class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque()
        queue.append(endWord)
        wmap = set()
        wmap.add(endWord)

        wset = set(wordList)
        wset.add(beginWord)

        if endWord not in wset:
            return 0

        count = 1
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == beginWord:
                    return count

                for index in range(len(word)):
                    pattern = word[:index] + "*" + word[index + 1:]
                    for words in wset:
                        wordspattern = words[:index] + "*" + words[index + 1:]
                        if wordspattern == pattern and words not in wmap:
                            print("here")
                            queue.append(words)
                            wmap.add(words)
            count += 1
        return 0