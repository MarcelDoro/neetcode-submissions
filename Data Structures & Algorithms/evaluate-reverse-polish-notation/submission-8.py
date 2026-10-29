class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for sym in tokens:
            print(stack)
            if sym != '+' and sym != '-' and sym != '*' and sym != '/':
                stack.append(sym)
            else:
                a = stack.pop()
                b = stack.pop()
                if sym == '+':
                    stack.append(str(int(b) + int(a)))
                elif sym == '-':
                    stack.append(str(int(b) - int(a)))
                elif sym == '*':
                    stack.append(str(int(b) * int(a)))
                elif sym == '/':
                    stack.append(str(int(int(b) / int(a))))
        
        return int(stack.pop())