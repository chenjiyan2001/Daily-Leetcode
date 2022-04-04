class NumArray:
    # [题解]1. O(logn) t:1196ms(53%) O(n) m:30.7M(42%) 树状数组
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.treeList = [0 for _ in range(self.n + 10)]
        for i in range(self.n):
            self.add(i + 1, nums[i])

    def lowbit(self, x: int):
        return x & (-x)

    def add(self, i: int, u: int):
        while i <= self.n:
            self.treeList[i] += u
            i += self.lowbit(i)
    
    def query(self, i: int):
        ans = 0
        while i > 0:
            ans += self.treeList[i]
            i -= self.lowbit(i)
        return ans

    def update(self, index: int, val: int) -> None:
        self.add(index + 1, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.query(right + 1) - self.query(left)