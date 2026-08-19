class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = { c : set() for word in words for c in word }
        
        def compare_words(word1: str, word2: str) -> bool:
            l = min(len(word1), len(word2))

            for i in range(l):
                if word1[i] != word2[i]:
                    adj[word1[i]].add(word2[i])
                    return True

            if len(word1) > len(word2):
                return False

        for i in range(len(words) - 1):
            if compare_words(words[i], words[i + 1]) == False:
                return ""

        res = []
        visited = {} # True - previously visited, False - visited during current path

        def dfs(c: str) -> bool:
            if c in visited:
                return visited[c]

            visited[c] = False
            for neighbour in adj[c]:
                if dfs(neighbour) == False:
                    return ""
            
            visited[c] = True
            res.append(c)
            return True

        
        for c in adj:
            if dfs(c) == False:
                return ''

        return ''.join(res[::-1])
        