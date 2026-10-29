class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

        List<List<Integer>> sumOfThree = new ArrayList<>();

        for (int i=0; i<nums.length; i++) {
            for (int j=i+1; j<nums.length; j++) {
                for (int k=j+1; k<nums.length; k++) {
                    if (nums[i] + nums[j] + nums[k] == 0) {
                        List<Integer> numbers = new ArrayList<>();
                        numbers.add(nums[i]);
                        numbers.add(nums[j]);
                        numbers.add(nums[k]);
                        numbers.sort(null);
                        if (!sumOfThree.contains(numbers)) sumOfThree.add(numbers);
                    }
                }
            }
        }
        return sumOfThree;
    }
}
