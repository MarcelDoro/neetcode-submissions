class Solution {
    public boolean isValid(String s) {
        Stack <Character> stack = new Stack<>();
        for (Character c : s.toCharArray()) {
            if (c == '[' || c == '(' || c == '{') {
                stack.push(c);
            }
            else if (!stack.empty()) {
                if (stack.peek() == '(' && c == ')' 
                ||  stack.peek() == '{' && c == '}' 
                ||  stack.peek() == '[' && c == ']' ) stack.pop();
                else return false;
            }
            else return false;
        }
        if (stack.empty()) return true;
        else return false;        
    }
}
