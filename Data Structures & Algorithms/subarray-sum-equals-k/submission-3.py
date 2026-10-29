class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_count = {0 : 1}
        curr_sum = 0
        for n in nums:
            curr_sum += n
            if curr_sum - k in prefix_count:
                res += prefix_count[curr_sum - k]
            
            prefix_count[curr_sum] = prefix_count.get(curr_sum, 0) + 1

        return res
           
