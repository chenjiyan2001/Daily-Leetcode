class Solution:
    # 1. O(n) t:244ms(50%) O(1) m:23.2M(70%) DP
    def maxProfit(self, prices: List[int]) -> int:
        sm, ans = prices[0], 0
        for p in prices:
            ans = max(ans, p - sm)
            sm = min(p, sm)
        return ans