class Solution {
    public int lengthOfLongestSubstring(String s) {
        int lenMax = 0;

        for (int i=0; i<s.length(); i++) {
            Set<Character> characters = new HashSet<>();
            int len = 1;
            if (len > lenMax) lenMax = len;
            characters.add(s.charAt(i));
            for (int j=i+1; j<s.length(); j++) {
                if (! characters.contains(s.charAt(j))) {
                    characters.add(s.charAt(j));
                    len++;
                    if (len > lenMax) lenMax = len;
                } else break;
            }
        }
        return lenMax;
    }
}
