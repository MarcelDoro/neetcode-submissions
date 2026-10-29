class MinStack:

    def __init__(self):
        self.stack = []
        self.mini_stack = []
        self.mini = float("inf")

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.mini_stack[-1] if self.mini_stack else val)
        self.mini_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.mini_stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        print(self.stack)
        print(self.mini_stack)
        return self.mini_stack[-1]
        
        
