class Solution:
    # 1. O(mn) t:28ms(96%) O(mn) m:14.8M(86%) 动态规划
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                dp[i][j] += (dp[i-1][j] if 0 <= i-1 < m else 0) + (dp[i][j-1] if 0 <= j-1 < n else 0)
        return dp[m-1][n-1]