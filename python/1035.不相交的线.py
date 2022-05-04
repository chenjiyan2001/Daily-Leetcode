class Solution:
    # 1. O(mn) t:164ms(90%) O(mn) m:15.4(48%) 动态规划
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n+1) for i in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]

    # 2. O(mn) t:352ms(5%) O(mn) m:59.3M(5%) 动态规划递归写法
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        @lru_cache(None)
        def dfs(i, j):
            if i == 0 or j == 0:
                return 0
            if nums1[i-1] == nums2[j-1]:
                return dfs(i-1, j-1) + 1
            else:
                return max(dfs(i, j-1), dfs(i-1, j))
        return dfs(m, n)