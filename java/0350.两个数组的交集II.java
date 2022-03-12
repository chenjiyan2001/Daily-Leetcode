class Solution {
    // 1. O(n) t:2ms(87%) O(1) m:41.2M(40%) 双指针
    public int[] intersect(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        int m = nums1.length, n = nums2.length;
        int i = 0, j = 0, idx = 0;
        int[] ans = new int[Math.min(m, n)];
        while (i < m && j < n) {
            if (nums1[i] == nums2[j]) {
                ans[idx] = nums1[i];
                i++;
                j++;
                idx++;
            }else if (nums1[i] < nums2[j]) {
                i++;
            }else{
                j++;
            }
        }
        return Arrays.copyOfRange(ans, 0, idx); 
    }
}