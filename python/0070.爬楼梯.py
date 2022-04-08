class Solution:
    # 1. O(n) t:36ms(60%) O(1) m:14.9M(69%) DP
    def climbStairs(self, n: int) -> int:
        dp0, dp1, ans = 1, 2, 0
        if n <= 2: return n
        for i in range(n - 2):
            ans = dp0 + dp1
            dp0, dp1 = dp1, ans
        return ans