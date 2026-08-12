class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [ [] for _ in range(n + 1) ]
        for u, v, t in times:
            adj[u].append((v, t))

        min_times = { i : sys.maxsize for i in range(n + 1) }
        def dfs(node: int, time: int) -> None:            
            min_times[node] = min(min_times[node], time)

            for neighbour, dt in adj[node]:
                if time + dt < min_times[neighbour]:
                    dfs(neighbour, time + dt)


        dfs(k, 0)

        if sys.maxsize in list(min_times.values())[1:]:
            return -1
        else:            
            return max(list(min_times.values())[1:])