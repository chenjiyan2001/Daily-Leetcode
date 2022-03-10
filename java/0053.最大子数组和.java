class Solution {
    // [题解]1. O(n) t:1ms(100%) O(1) m:50.2M(43.4%) 动态规划
    public int maxSubArray(int[] nums) {
        int pre = 0, ans = nums[0];
        for (int num : nums) {
            pre = Math.max(pre + num, num);
            ans = Math.max(ans, pre);
        }
        return ans;
    }
}