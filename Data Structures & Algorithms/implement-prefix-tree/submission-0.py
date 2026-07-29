class TreeNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        node = self.root
        
        for i in range(len(word)):
            c = word[i]

            if node.children.get(c) == None:
                node.children[c] = TreeNode()
            
            node = node.children[c]                    
            
            if i == len(word) - 1:
                node.end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root

        for c in word:
            if node.children.get(c) == None:
                return False
            else:
                node = node.children[c]
        
        return node.end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for c in prefix:
            if node.children.get(c) == None:
                return False
            else:
                node = node.children[c]
        
        return True        