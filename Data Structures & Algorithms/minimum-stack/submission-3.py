class MinStack:

    def __init__(self):
        self.stack = []
        self.otherStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.otherStack.append(min(val, self.otherStack[-1] if self.otherStack else val))

    def pop(self) -> None:
        self.stack.pop()
        self.otherStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.otherStack[-1]