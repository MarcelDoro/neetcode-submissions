class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        node = self.root
        
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            
            node = node.children[c]
        
        node.end_of_word = True


    def search(self, word: str) -> bool:
        def dfs_search(word, starting_node):
            node = starting_node

            for i in range(len(word)):
                c = word[i]

                if c == '.':
                    for child in node.children.values():
                        if dfs_search(word[i + 1:], child) == True:
                            return True

                    return False
                else:
                    if c not in node.children:
                        return False

                    node = node.children[c]

            return node.end_of_word

        return dfs_search(word, self.root)
