class Solution {
    // 1. O(n) t:0ms(100%) m:36M(39%)
    public int dominantIndex(int[] nums) {
        int n = nums.length;
        if (n == 1) return 0;
        int m = -1, s = 0, idx = 0;
        for (int i = 0; i < n; i++){
            if (nums[i] > m){
                s = m;
                m = nums[i];
                idx = i;
            }else if(nums[i] > s){
                s = nums[i];
            }
        }
        return m >= 2 * s ? idx : -1;
    }
}