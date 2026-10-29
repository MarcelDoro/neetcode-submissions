class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> Occur = new HashSet<>();
        for (Integer num : nums) {
            Occur.add(num);
        }

        int lengthMax = 0;

        for (Integer num : Occur) {
            if (!Occur.contains(num - 1)) {
                int length = 1;
                while(Occur.contains(num + 1)) {
                    num++;
                    length++;
                }
                if(length > lengthMax) lengthMax = length;
            }
        }
        return lengthMax;
    }
}
