class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = [False] * (n + 1)
        cycle = set()
        cycle_start = -1

        def dfs(node: int, parent: int) -> bool:
            nonlocal cycle_start

            if visit[node]:
                cycle_start = node
                return True

            visit[node] = True
            for neighbour in adj[node]:
                if neighbour == parent:
                    continue
                if dfs(neighbour, node):
                    if cycle_start != -1:
                        cycle.add(node)
                    if cycle_start == node:
                        cycle_start = -1
                    return True

            return False
            

        dfs(1, -1)

        for n1, n2 in reversed(edges):
            if n1 in cycle and n2 in cycle:
                return [n1, n2]

        return []

