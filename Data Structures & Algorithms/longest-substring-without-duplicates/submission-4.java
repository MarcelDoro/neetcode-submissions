class Solution {
    public int lengthOfLongestSubstring(String s) {
        int lenMax = 0;

        Set <Character> characters = new HashSet<>();
        int l = 0, r = 0;
        int len = 0;
        while (r < s.length()) {
            if (! characters.contains(s.charAt(r))) {
                characters.add(s.charAt(r));
                len++;
                r++;
            } else {
                len--;
                characters.remove(s.charAt(l));
                l++;              
            }
            if (len > lenMax) lenMax = len;
        }


        return lenMax;
    }
}
