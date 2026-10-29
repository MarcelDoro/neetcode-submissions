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
                    print("1st loop:", area)
                    if area > max_area:
                        max_area = area
                starting_index = i
                while starting_index > 0 and heights[starting_index - 1] >= heights[i]:
                    starting_index -= 1
                print(starting_index,heights[i])
                stack.append((starting_index,heights[i]))
        
        for index, height in stack:
            area = (n - index) * height
            print("2nd loop:", area)
            if area > max_area:
                max_area = area

        return max_area