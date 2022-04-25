class Solution:
    # 1. O(n) t:104ms(31%) O(n) m:25M(14%) 哈希表
    def __init__(self, nums: List[int]):
        self.nums = defaultdict(list)
        for idx, num in enumerate(nums):
            self.nums[num].append(idx)

    def pick(self, target: int) -> int:
        return random.choice(self.nums[target])
    
    # [题解]2. O(n) t:68ms(98%) O(1) m:18.5M(35%) 蓄水池抽样
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        ans, cnt = 0, 0
        for i, num in enumerate(self.nums):
            if num == target:
                cnt += 1
                if randrange(cnt) == 0:
                    ans = i
        return ans