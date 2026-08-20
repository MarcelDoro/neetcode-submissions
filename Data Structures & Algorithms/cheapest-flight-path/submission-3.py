class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [ [] for _ in range(n) ]

        for flight in flights:
            s, d, p = flight
            adj[s].append([d, p])

        min_price = [float('inf')] * n
        min_price[src] = 0

        q = deque([(src, 0)])
        stops = 0

        while q and stops <= k:
            for _ in range(len(q)):
                node, price = q.popleft()

                for nei, p in adj[node]:
                    new_price = price + p

                    if new_price < min_price[nei]:
                        min_price[nei] = new_price
                        q.append((nei, new_price))

            stops += 1

        return min_price[dst] if min_price[dst] != float('inf') else -1
