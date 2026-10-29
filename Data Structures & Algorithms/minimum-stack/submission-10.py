class MinStack:

    def __init__(self):
        self.stack = []
        self.mini_stack = []
        self.mini = float("inf")

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.mini:
            self.mini = val
        self.mini_stack.append(self.mini)

    def pop(self) -> None:
        del self.stack[-1]       
        if self.mini_stack[-1] == self.mini:
            if len(self.stack) >= 2:
                self.mini = self.mini_stack[-2]
            else:
                self.mini = float("inf")
        del self.mini_stack[-1]

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        print(self.stack)
        print(self.mini_stack)
        return self.mini_stack[-1]
        
        
