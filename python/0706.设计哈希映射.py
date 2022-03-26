class MyHashMap:
    # [题解]1. O(1) t:156ms(76%) O(n) m:18.6M(37%) 链表
    def __init__(self):
        self.base = 769 # 取质数来尽量避免冲突
        self.data = [[] for i in range(self.base)]
    
    def hash(self, key):
        return key % self.base

    def put(self, key: int, value: int) -> None:
        h = self.hash(key)
        for item in self.data[h]:
            if item[0] == key:
                item[1] = value
                return
        self.data[h].append([key, value])


    def get(self, key: int) -> int:
        h = self.hash(key)
        for item in self.data[h]:
            if item[0] == key:
                return item[1]
        return -1


    def remove(self, key: int) -> None:
        h = self.hash(key)
        for i, item in enumerate(self.data[h]):
            if item[0] == key:
                self.data[h].pop(i)
                return