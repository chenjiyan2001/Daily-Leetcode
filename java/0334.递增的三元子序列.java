class Solution {
    // // 1. O(n^2) 动态规划 超时
    // public boolean increasingTriplet(int[] nums) {
    //     int n = nums.length, max = 1;
    //     int[] dp = new int[n + 1];
    //     Arrays.fill(dp, 1);
    //     for (int i = 0; i < n; i++){
    //         for (int j = 0; j < i; i++){
    //             if (nums[j] < nums[i] && dp[i] < dp[j] + 1){
    //                 dp[i] = dp[j] + 1;
    //             }
    //         }
    //         max = Math.max(dp[i], max);
    //         if (max >= 3) return true;
    //     }
    //     return false;
    // }

    // // 2. O(nlogn) t:10ms(7%) O(n) m:78.9M(94%) 贪心+二分
    // public boolean increasingTriplet(int[] nums) {
    //     int n = nums.length, ans = 1;
    //     int[] f = new int[n + 1];
    //     Arrays.fill(f, 0x3f3f3f3f);
    //     for (int i = 0; i < n; i++) {
    //         int t = nums[i];
    //         int l = 1, r = i + 1;
    //         while (l < r) {
    //             int mid = l + r >> 1;
    //             if (f[mid] >= t) r = mid;
    //             else l = mid + 1;
    //         }
    //         f[r] = t;
    //         ans = Math.max(ans, r);
    //     }
    //     return ans >= 3;
    // }

    // 3. O(n) t:3ms(39%) t:O(1) m:79.3M(14%) 定长子序列
    public boolean increasingTriplet(int[] nums) {
        int n = nums.length;
        long[] f = new long[3];
        f[1] = f[2] = (int)1e19;
        for (int i = 0; i < n; i++){
            int t = nums[i];
            if (f[2] < t) return true;
            else if (f[1] < t && t < f[2]) f[2] = t;
            else if (f[1] > t) f[1] = t;
        }
        return false;
    }
}