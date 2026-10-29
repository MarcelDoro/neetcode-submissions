class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

        List<List<Integer>> sumOfThree = new ArrayList<>();

        Arrays.sort(nums);
        for (int i=0; i<nums.length-2; i++) {
            int j = i + 1, k = nums.length - 1;
            while (j < k) {
                if (- nums[i] > nums[j] + nums[k]) {
                    j++;
                }
                else if (- nums[i] < nums[j] + nums[k]) {
                    k--;
                }
                else {
                    List<Integer> numbers = new ArrayList<>();
                    numbers.add(nums[i]);
                    numbers.add(nums[j]);
                    numbers.add(nums[k]);
                    numbers.sort(null);
                    if (!sumOfThree.contains(numbers)) sumOfThree.add(numbers);
                    j++;
                    k--;
                }
            }

        }
        return sumOfThree;
    }
}
