class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i: int, total: int) -> int:
            if total == amount:
                return 1            
            if total > amount:                
                return 0
            if i >= len(coins):
                return 0
            if (i, total) in memo:
                return memo[(i, total)]

            memo[(i, total)] = dfs(i, total + coins[i]) + dfs(i + 1, total)
            return memo[(i, total)]

        
        return dfs(0, 0)
