class WordDictionary:

    def __init__(self):
        self.words = []

    def addWord(self, word: str) -> None:
        self.words.append(word)

    def search(self, word: str) -> bool:
        n = len(word)
        for w in self.words:
            if len(w) != len(word):
                continue
            i = 0
            while i < n:
                if w[i] == word[i] or word[i] == ".":
                    i+=1
                else:
                    break
            if i == n:
                return True
        return False
        


# Yo9ur WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)