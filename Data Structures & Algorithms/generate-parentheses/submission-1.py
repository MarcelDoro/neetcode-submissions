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

        tmp = ''
        def dfs(i):
            nonlocal tmp            

            if i >= 2 * n:                
                if valid_parentheses(tmp):
                    res.append(tmp)

                return
            
            tmp += '('
            dfs(i + 1)
            tmp = tmp[:-1]            
            tmp += ')'
            dfs(i + 1)
            tmp = tmp[:-1]

        dfs(0)
        return res