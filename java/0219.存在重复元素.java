class Solution {
    // 1. O(n) t:18ms O(k) m:53M(23%) 滑动窗口+hash
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> set = new HashSet();
        for (int i = 0; i < nums.length; i++){
            if (i > k) set.remove(nums[i - k - 1]);
            if (set.contains(nums[i])) return true;
            set.add(nums[i]);
        }
        return false;
    }
}