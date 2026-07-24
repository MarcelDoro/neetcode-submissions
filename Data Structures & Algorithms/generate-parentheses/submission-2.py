class Solution:
    def generateParenthesis(self, n: int) -> List[str]:        
        def valid_parentheses(tmp: str) -> True | False:
            stack = []
            for c in tmp:
                if stack and stack[-1] == '(' and c == ')':
                    stack.pop()
                else:
                    stack.append(c)

            if not stack:
                return True
            else:
                return False

        res = []
        def dfs(i, curr):         
            if i >= 2 * n:                
                if valid_parentheses(curr):
                    res.append(curr)

                return
            
            dfs(i + 1, curr + '(')
            dfs(i + 1, curr + ')')

        dfs(0, '')
        return res