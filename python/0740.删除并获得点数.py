class Solution:
    # [题解]1. O(nlogn) t:52ms(34%) O(M) m:17.5M(5%) DP
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        m = max(nums) + 1
        all = [0] * m
        for k, v in cnt.items():
            all[k] = v  
        dp = [[0] * 2 for _ in range(m)]
        for i in range(1, m):
            dp[i][0] = max(dp[i-1])
            dp[i][1] = dp[i-1][0] + all[i] * i
        return max(dp[i])