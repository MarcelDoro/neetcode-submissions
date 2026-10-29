class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        for i in range(n):
            min_height = heights[i]
            for j in range(i, n):
                if heights[j] < min_height:
                    min_height = heights[j]
                
                if min_height * (j - i + 1) > max_area:
                    max_area = min_height * (j - i + 1)
        
        return max_area

