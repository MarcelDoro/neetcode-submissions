class Solution {
    public int maxProfit(int[] prices) {
        int maxP = 0;

        int l = 0;
        int r = 1;
        while (r < prices.length) {
            if (prices[l] < prices[r]) {
                maxP = Math.max(maxP, prices[r] - prices[l]);
            } else {
                l = r;
            }
            r++;
        }
        return maxP;
    }
}
