class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def can_convert(word1: str, word2: str) -> bool:
            differences: int = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    differences += 1
                    if differences > 1:
                        return False

            return True

        wordList.insert(0, beginWord)
        adj: dict[str, str] = { word : [] for word in wordList }

        for i in range(len(wordList)):
            word1: str = wordList[i]
            for j in range(i + 1, len(wordList)):
                word2: str = wordList[j]
                if can_convert(word1, word2):
                    adj[word1].append(word2)
                    adj[word2].append(word1)

        visited = set()
        def bfs(starting_word: str) -> int:
            q = deque()
            q.append(starting_word)            
            counter = 1

            while q:
                for i in range(len(q)):
                    word = q.popleft()
                    visited.add(word)
                    if word == endWord:
                        return counter

                    for neighbour in adj[word]:
                        if not neighbour in visited:
                            q.append(neighbour)                        

                counter += 1

            return 0

        return bfs(beginWord)