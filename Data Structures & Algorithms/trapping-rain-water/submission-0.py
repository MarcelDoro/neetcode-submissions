class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        for i in range(1, n - 1):
            max_l = height[i - 1]         
            l = i - 1
            while l >= 0:
                if height[l] > max_l:
                    max_l = height[l]
                l -= 1

            max_r = height[i + 1]
            r = i + 1
            while r < n:
                if height[r] > max_r:
                    max_r = height[r]
                r += 1

            if max_r > height[i] and max_l > height[i]:
                water += min(max_r, max_l) - height[i]
        
        return water
            

            

        