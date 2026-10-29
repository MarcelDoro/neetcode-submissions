class Solution {

    public String encode(List<String> strs) {
        String ans = "";
        for (String s : strs) {
            ans = ans + s + "☺";
        }

        return ans;
    }

    public List<String> decode(String str) {
        List<String> ans = new ArrayList<>();
        String s = "";

        for (char c : str.toCharArray()) {
            if (c == '☺') {
                ans.add(s);
                s = "";
            }
            else {
                s = s + c;
            }
        }

        return ans;
    }
}
