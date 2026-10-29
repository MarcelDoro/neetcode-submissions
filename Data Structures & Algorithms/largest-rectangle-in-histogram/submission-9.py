class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_area = 0

        for i in range(n):
            if len(stack) == 0:
                stack.append((i, heights[i]))
            else:
                while len(stack) > 0 and heights[i] < stack[-1][1]:
                    index, height = stack.pop()
                    area = (i - index) * height
                    if area > max_area:
                        max_area = area
                starting_i = i
                while starting_i > 0 and heights[starting_i - 1] >= heights[i]:
                    starting_i -= 1
                stack.append((starting_i,heights[i]))
        
        for index, height in stack:
            area = (n - index) * height
            if area > max_area:
                max_area = area

        return max_area