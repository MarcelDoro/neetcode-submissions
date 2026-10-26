class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def max_profit(i: int, hold: bool, profit: int) -> None:
            if (i, hold) in cache:
                return cache[(i, hold)]

            if i == len(prices):          
                return 0

            if hold:                
                sell = prices[i] + max_profit(i + 1, False, profit)
                skip = max_profit(i + 1, True, profit)

                cache[(i, hold)] = max(sell, skip)
                return cache[(i, hold)]
            else:                
                buy = -prices[i] + max_profit(i + 1, True, profit)
                skip = max_profit(i + 1, False, profit)

                cache[(i, hold)] = max(buy, skip)
                return cache[(i, hold)]
        
        return max_profit(0, False, 0)
