class MedianFinder:

    def __init__(self):
        self.small_heap = [] #max_heap
        self.large_heap = [] #min_heap
        heapq.heapify(self.small_heap)
        heapq.heapify(self.large_heap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_heap, -num)        
        if len(self.small_heap) - len(self.large_heap) > 1:
            max_val = heapq.heappop(self.small_heap)            
            heapq.heappush(self.large_heap, -max_val)
        elif len(self.small_heap) > 0 and len(self.large_heap) > 0:
            maxi, mini = -heapq.nsmallest(1, self.small_heap)[0], heapq.nsmallest(1, self.large_heap)[0]
            if mini < maxi:
                max_val = heapq.heappop(self.small_heap)            
                heapq.heappush(self.large_heap, -max_val)
                if len(self.large_heap) - len(self.small_heap) > 1:
                    min_val = heapq.heappop(self.large_heap)
                    heapq.heappush(self.small_heap, -min_val)

        print(self.small_heap)
        print(self.large_heap)

    def findMedian(self) -> float:
        if len(self.small_heap) > len(self.large_heap):
            return -heapq.nsmallest(1, self.small_heap)[0]
        elif len(self.small_heap) < len(self.large_heap):
            return heapq.nsmallest(1, self.large_heap)[0]
        else:
            a, b = heapq.nsmallest(1, self.small_heap)[0], heapq.nsmallest(1, self.large_heap)[0]
            return (-a + b) / 2