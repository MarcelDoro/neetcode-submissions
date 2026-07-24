class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(opened, closed, text):
            if opened == closed == n:
                res.append(text)

            if opened < n:
                backtrack(opened + 1, closed, text + '(')

            if opened > closed:
                backtrack(opened, closed + 1, text + ')')

        backtrack(0, 0, '')
        return res