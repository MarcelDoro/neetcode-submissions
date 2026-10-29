class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> PotDiff = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            int diff = target - nums[i];
            if(PotDiff.containsKey(diff)) return new int[]{PotDiff.get(diff), i};

            PotDiff.put(nums[i],i);
        }
        return new int[]{};
    }
}
