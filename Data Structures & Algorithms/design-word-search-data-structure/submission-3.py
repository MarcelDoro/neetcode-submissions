class WordDictionary:

    def __init__(self):
        self.words = []

    def addWord(self, word: str) -> None:
        self.words.append(word)

    def search(self, word: str) -> bool:
        for el in self.words:
            if len(word) == len(el):
                i = 0
                while i < len(word):
                    if word[i] == '.':
                        i += 1
                        continue
                    
                    if word[i] != el[i]:
                        break

                    i += 1

                if i == len(word):
                    return True

        return False