class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] ans = new int[nums.length];
        int[] pre = new int[nums.length];
        int[] post = new int[nums.length];

        int prod = 1;
        for (int i=0; i<nums.length; i++) {
            prod *= nums[i];
            pre[i] = prod;
        }

        prod = 1;
        for (int i=nums.length - 1; i>=0; i--) {
            prod *= nums[i];
            post[i] = prod;
        }

        ans[0] = post[1];
        ans[nums.length - 1] = pre[nums.length - 2];
        for (int i=1; i<nums.length - 1; i++) {
            ans[i] = pre[i - 1] * post[i + 1];
        }

        return ans;
    }
}  
