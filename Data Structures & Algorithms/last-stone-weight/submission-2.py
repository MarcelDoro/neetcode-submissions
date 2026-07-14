class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            new_stone = first - second
            heapq.heappush(stones, new_stone) 
        
        return -stones[0] if len(stones) > 0 else 0