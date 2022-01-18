class Solution:
    # # 1. O(n) t:24ms(97%) m:14.9M(84%) 循环
    # def dominantIndex(self, nums: List[int]) -> int:
    #     f, s, idx = -1, 0, 0
    #     for i, num in enumerate(nums):
    #         if num > f:
    #             s, f = f, num
    #             idx = i
    #         elif num > s:
    #             s = num
    #     if f >= 2*s:
    #         return idx
    #     else:
    #         return -1
        
    # 2. t:32ms(65%) m:15.1M(15%) list方法
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        m = max(nums)
        idx = nums.index(m)
        nums.pop(idx)
        s = max(nums)
        return idx if m >= 2*s else -1
