class Solution:
    # [题解]1. O(n) t:36ms(63%) O(n) m:14.9M(56%) 动态规划
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        dp = [0 for _ in range(n+1)]
        dp[1] = nums[0]
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], nums[i-1] + dp[i-2])
        return dp[n]