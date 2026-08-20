import copy


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        min_prices = [float('inf')] * n
        min_prices[src] = 0

        stops = 0
        while stops < k + 1:
            tmp_min_prices = copy.copy(min_prices)
            for flight in flights:
                start, end, price = flight

                if min_prices[start] + price < tmp_min_prices[end]:
                    tmp_min_prices[end] = min_prices[start] + price

            for i in range(len(tmp_min_prices)):
                min_prices[i] = tmp_min_prices[i]

            stops += 1

        return min_prices[dst] if min_prices[dst] != float('inf') else -1