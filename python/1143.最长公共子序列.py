class Solution:
    # [题解]1. O(mn) t:356ms(64%) O(mn) m:23.6M(26%) 动态规划
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]

    # [题解]2. O(mn) t:716ms(5%) O(mn) m:138.5M(5%) 动态规划(递归)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if not i or not j: return 0
            if text1[i-1] == text2[j-1]: return dfs(i-1, j-1) + 1
            return max(dfs(i-1, j), dfs(i, j-1))
        return dfs(len(text1), len(text2))