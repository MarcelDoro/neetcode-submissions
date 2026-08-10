class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj ={ i : [] for i in range(n) }

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()
        def dfs(node):
            for neighbour in adj[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour)


        components = 0
        for node in range(n):
            if node in visited:
                continue

            visited.add(node)
            dfs(node)
            components += 1

        return components
