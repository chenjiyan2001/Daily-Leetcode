class RandomizedSet:
    # [题解]1. O(1) t:648(模式6%) O(1) m:51.3M(5%) 变长数组+哈希表
    def __init__(self):
        self.nums = []
        self.idx_map = {}

    def insert(self, val: int) -> bool:
        if val not in self.idx_map:
            self.idx_map[val] = len(self.nums)
            self.nums.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.idx_map:
            swap_val, idx = self.nums[-1], self.idx_map[val]
            self.nums[idx] = swap_val
            self.idx_map[swap_val] = idx
            del self.idx_map[val]
            self.nums.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        return choice(self.nums)