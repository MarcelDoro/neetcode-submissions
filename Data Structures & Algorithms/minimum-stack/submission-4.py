class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        print(self.stack)
        print("removing:",self.stack[len(self.stack) - 1])
        del self.stack[-1]

    def top(self) -> int:
        print(self.stack)
        print("ret:", self.stack[len(self.stack) - 1])
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        mini = self.stack[0]
        for n in self.stack:
            if n < mini:
                mini = n
        return mini 
        
