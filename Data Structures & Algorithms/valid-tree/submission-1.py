class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adj = { i : [] for i in range(n) }
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        visited = set()
        def dfs(val: int, prev: int):
            if val in visited:
                return False

            visited.add(val)

            for node_val in adj[val]:
                if node_val != prev:                
                    if dfs(node_val, val) == False:
                        return False

            return True        

        return dfs(0, -1) and n == len(visited)
                   