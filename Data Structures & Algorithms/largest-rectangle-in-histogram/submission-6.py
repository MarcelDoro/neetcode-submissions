class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0

        for i in range(n):
            start = i
            end = i
            while start > 0 and heights[start - 1] >= heights[i]:
                start -= 1
            
            while end < n - 1 and heights[end + 1] >= heights[i]:
                end += 1

            area = (end - start + 1) * heights[i]
            if area > max_area:
                max_area = area

        return max_area