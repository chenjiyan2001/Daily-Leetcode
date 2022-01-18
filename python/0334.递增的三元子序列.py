class Solution:
    # # 1. O(n^2) 超时 dp
    # def increasingTriplet(self, nums: List[int]) -> bool:
    #     length = len(nums)
    #     dp = [1] * length
    #     for i in range(length):
    #         for j in range(i):
    #             if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
    #                 dp[i] = dp[j] + 1
    #         if max(dp) >= 3: return True
    #     return False
    
    # # 2. O(nlogn) t:876ms(5%) m:24.1M(29%) 贪心+二分
    # def increasingTriplet(self, nums: List[int]) -> bool:
    #     length, ans = len(nums), 1
    #     slow = [inf] * (length + 1)
    #     for i in range(length):
    #         l, r, t = 1, i + 1, nums[i]
    #         while l < r:
    #             m = (l + r)//2
    #             if t <= slow[m]:
    #                 r = m
    #             else:
    #                 l = m + 1
    #         slow[r] = t
    #         ans = max(ans, r)
    #     return ans >= 3


    # 3. O(n) t:48ms(99%) m:23.8M(96%) 仅维护长度为2的数组
    def increasingTriplet(self, nums: List[int]) -> bool:
        small = mid = inf
        for num in nums:
            if num <= small:
                small = num
            elif num <= mid:
                mid = num
            else:
                return True
        return False