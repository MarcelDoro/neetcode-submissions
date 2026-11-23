class StockSpanner:

    def __init__(self):
        self.prices = [] # (price, span)
        
    def next(self, price: int) -> int:
        span = 1
        while self.prices and price >= self.prices[-1][0]:            
            span += self.prices[-1][1]
            del self.prices[-1]

        self.prices.append((price, span))

        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)