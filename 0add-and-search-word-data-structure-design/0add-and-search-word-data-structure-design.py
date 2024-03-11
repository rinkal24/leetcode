class WordDictionary:

    def __init__(self):
        self.wordList = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.wordList[len(word)].add(word)

    def search(self, word: str) -> bool:
        m = len(word)
        for d in self.wordList[m]:
            i = 0
            while i < m and (d[i] == word[i] or word[i] == '.'):
                i += 1
            if i == m:
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


