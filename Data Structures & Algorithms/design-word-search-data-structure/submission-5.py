class WordNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = WordNode()


    def addWord(self, word: str) -> None:
        node = self.root
        
        for i in range(len(word)):
            c = word[i]

            if node.children.get(c) == None:
                node.children[c] = WordNode()
            
            node = node.children[c]
        
        node.end_of_word = True


    def search2(self, word, starting_node):
        node = starting_node

        for i in range(len(word)):
            c = word[i]

            if c == '.':
                for key in node.children.keys():
                    if self.search2(word[i + 1:], node.children[key]) == True:
                        return True
                        
                return False
            else:
                if node.children.get(c) == None:
                    return False

                node = node.children[c]

        return node.end_of_word


    def search(self, word: str) -> bool:
        return self.search2(word, self.root)

        
        
