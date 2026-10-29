class Solution {
    public int maxArea(int[] heights) {
        int max = 0;
        int i = 0, j = heights.length - 1;
        while (i < j) {
            int area = (j - i) * Math.min(heights[i], heights[j]);
            if (area > max) max = area;
            if (heights[i] < heights[j]) {
                i++;
            } else {
                j--;
            }
        }
        return max;
    }
}
