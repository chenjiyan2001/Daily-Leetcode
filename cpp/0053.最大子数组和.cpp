class Solution {
public:
    // [题解]1. O(n) t:80ms(90%) O(n) M:66.1M(85%) 动态规划
    int maxSubArray(vector<int>& nums) {
        int ans = nums[0], pre = 0;
        for (auto num : nums) {
            pre = max(pre + num, num);
            ans = max(ans, pre);
        }
        return ans;
    }
};