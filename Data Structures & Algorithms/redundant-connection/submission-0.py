class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = { i : [] for i in range(1, n + 1) }

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def is_every_node_connected(node: int) -> bool:
            visited.add(node)

            for neighbour in adj[node]:
                if not neighbour in visited:
                    is_every_node_connected(neighbour)
            
            return len(visited) == n


        for n1, n2 in edges:
            tmp1 = n1
            tmp2 = n2

            adj[n1].remove(n2)
            adj[n2].remove(n1)

            visited = set()
            if is_every_node_connected(1) == True:
                res = [tmp1, tmp2]

            adj[n1].append(n2)
            adj[n2].append(n1)

        return res  
