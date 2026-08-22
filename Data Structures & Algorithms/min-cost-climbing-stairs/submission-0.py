class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        full_prices = [float('inf')] * (n + 1)
        full_prices[0] = 0
        full_prices[1] = 0

        for i in range(n):
            if i + 1 < len(full_prices) and full_prices[i] + cost[i] < full_prices[i + 1]:
                full_prices[i + 1] = full_prices[i] + cost[i]
            
            if i + 2 < len(full_prices) and full_prices[i] + cost[i] < full_prices[i + 2]:
                full_prices[i + 2] = full_prices[i] + cost[i]

        return full_prices[-1]
