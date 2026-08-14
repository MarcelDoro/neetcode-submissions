class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [ [] for _ in range(numCourses) ]

        for u, v in prerequisites:
            adj[u].append(v)

        res = []
        visited = [0 for _ in range(numCourses)] 

        def dfs(node: int) -> bool:
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True

            visited[node] = 1            

            for neighbour in adj[node]:
                if not dfs(neighbour):
                    return False

            res.append(node)
            visited[node] = 2

            return True


        for node in range(numCourses):
            if not dfs(node):
                return []

        return res

