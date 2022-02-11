class Solution {
    // 1. O(nlogn) t:4ms(100%) O(logn) m:41.6M(5%)
    public int minimumDifference(int[] nums, int k) {
        Arrays.sort(nums);
        int ans = nums[k - 1] - nums[0];
        for (int i = 0; i <= nums.length - k; i++){
            int diff = nums[i + k - 1] - nums[i];
            if (diff < ans){
                ans = diff; 
            }
        }
        return ans;
    }
}