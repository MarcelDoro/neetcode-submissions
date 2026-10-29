class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;

        int[] Tabs = new int[256];
        int[] Tabt = new int[256];

        for(int i=0; i<s.length() ;i++){
            int nums = (int) s.charAt(i);
            int numt = (int) t.charAt(i);
            Tabs[nums]++;
            Tabt[numt]++;
        }

        for(int i=0; i<255; i++){
            if(Tabs[i] != Tabt[i]) return false;
        }
        return true;
    }
}
