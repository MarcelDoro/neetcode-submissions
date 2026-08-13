class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [ [] for _ in range(numCourses) ]

        for v, u in prerequisites:
            adj[v].append(u)

        states = [0] * numCourses
        # 0 - unvisited, 1 - curently visited, 2 - reviously visited
                
        def dfs(node: int) -> bool:            
            if states[node] == 1:
                return False
            if states[node] == 2:
                return True

            states[node] = 1
            for neighbour in adj[node]:    
                if not dfs(neighbour):
                    return False
            
            states[node] = 2
            return True


        for n in range(numCourses):     
            if not dfs(n):
                return False

        return True
                