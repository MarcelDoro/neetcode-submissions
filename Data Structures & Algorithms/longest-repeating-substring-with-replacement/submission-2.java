class Solution {
    public int characterReplacement(String s, int k) {
        int lenMax = 0;

        for (int i=0; i<s.length(); i++) {
            HashMap<Character, Integer> characters = new HashMap<>();
            characters.put(s.charAt(i), characters.getOrDefault(s.charAt(i), 0) + 1);
            int max = 0;
            for (int j=i+1; j<s.length(); j++) {
                characters.put(s.charAt(j), characters.getOrDefault(s.charAt(j), 0) + 1);
                if (characters.get(s.charAt(j)) > max) max = characters.get(s.charAt(j));

                if (j - i + 1 - max <= k) {
                    if (j - i + 1> lenMax) {
                        lenMax = j - i + 1;
                    }
                }
            }
        }

        return lenMax;
    }
}
