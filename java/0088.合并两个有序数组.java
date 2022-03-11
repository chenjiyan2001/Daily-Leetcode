class Solution {
    // 1. O(m+n) t:0ms(100%) O(1) m:41.4M(19%) 双指针
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = nums1.length - 1;
        m--; n--;
        while (m >= 0 || n >= 0) {
            if (m < 0){
                nums1[i--] = nums2[n--];
            }else if (n < 0){
                nums1[i--] = nums1[m--];
            }else if (nums1[m] < nums2[n]){
                nums1[i--] = nums2[n--];
            }else{
                nums1[i--] = nums1[m--];
            }
        }
    }
}