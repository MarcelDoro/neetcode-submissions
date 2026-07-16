class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapq.heapify(nums)
        
        k_th = 0
        for i in range(k):
            k_th = heapq.heappop(nums)
        
        return -k_th