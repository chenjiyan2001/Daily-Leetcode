class Solution {
public:
    // 1. O(n) t:88ms(94%) O(1) m:91M(97%) DP
    int maxProfit(vector<int>& prices) {
        int sm = prices[0], ans = 0;
        for (int p : prices) {
            ans = max(ans, p - sm);
            sm = min(sm, p);
        }
        return ans;
    }
};