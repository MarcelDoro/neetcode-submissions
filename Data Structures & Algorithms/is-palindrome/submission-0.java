class Solution {
    public boolean isPalindrome(String s) {
        String forward = "";
        int i = 0;
        for (char c : s.toCharArray()) {
            if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9')) {
                forward = forward + c;
            }
            i++;
        }

        String backward = "";
        i = s.length() - 1;
        while (i >= 0) {
            if ((s.charAt(i) >= 'a' && s.charAt(i) <= 'z') || (s.charAt(i) >= 'A' && s.charAt(i) <= 'Z') || (s.charAt(i) >= '0' && s.charAt(i) <= '9')) {
                backward = backward + s.charAt(i);
            }
            i--;
        }

        String forw = "";
        String back = "";
        for (i=0; i<forward.length(); i++) {
            if (forward.charAt(i) >= 65 && forward.charAt(i) <= 90) {
                forw = forw + (char) ((int) forward.charAt(i) + 32);
            }
            else forw = forw + forward.charAt(i);
        }

        for (i=0; i<backward.length(); i++) {
            if (backward.charAt(i) >= 65 && backward.charAt(i) <= 90) {
                back = back + (char) ((int) backward.charAt(i) + 32);
            }
            else back = back + backward.charAt(i);
        }

        System.out.println(forw);
        System.out.println(back);

        if (forw.equals(back)) return true;
        else return false;
    }
}
