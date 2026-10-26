class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}        
        def calculate_max_profit(i: int, hold: bool) -> int:
            if (i, hold) in cache:
                return cache[(i, hold)]

            if i == len(prices):                
                return 0

            if hold:
                sell = prices[i] + calculate_max_profit(i + 1, False)
                skip = calculate_max_profit(i + 1, True)
                res = max(sell, skip)
            else:
                buy = -prices[i] + calculate_max_profit(i + 1, True)
                skip = calculate_max_profit(i + 1, False)
                res = max(buy, skip)

            cache[(i, hold)] = res
            return res

        return calculate_max_profit(0, False)
