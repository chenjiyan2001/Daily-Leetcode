class Solution {
    // 1. O(n) t:1ms(100%) O(1) m:57.6M(20%) DP
    public int maxProfit(int[] prices) {
        int sm = prices[0], ans = 0;
        for (int p : prices) {
            ans = Math.max(ans, p - sm);
            sm = Math.min(sm, p);
        }
        return ans;
    }
}