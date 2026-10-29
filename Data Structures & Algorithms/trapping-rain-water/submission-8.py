class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        max_l = []
        maxi_l = height[0]
        for i in range(n):
            if height[i] > maxi_l:
                maxi_l = height[i]
            max_l.append(maxi_l)

        max_r = []
        maxi_r = height[n - 1] 
        for i in range(n - 1, -1, -1):
            if height[i] > maxi_r:
                maxi_r = height[i]
            max_r.append(maxi_r)      
        max_r.reverse()

        for i in range(n):
            if height[i] < max_r[i] and height[i] < max_l[i]:
                water += min(max_r[i], max_l[i]) - height[i]

        return water

              