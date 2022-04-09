class MinStack:
    # [题解]1. O(1) t:84ms(24%) O(1) m:18.5M(31%) 辅助栈
    def __init__(self):
        self.stack = []
        self.minStack = [inf]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minStack.append(min(val, self.minStack[-1]))


    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]