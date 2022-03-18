# 1. O(n) t:40ms(28%) O(n) m:15M(75%)
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        while self.s2:
            self.s1.append(self.s2.pop())
        self.s1.append(x)


    def pop(self) -> int:
        while self.s1:
            self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        while self.s1:
            self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        if self.s1 or self.s2:
            return False
        else:
            return True

# [题解]2. O(均摊1) t:40ms(28%) O(n) m:15.2M(25%)
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)


    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return not (self.s1 or self.s2)