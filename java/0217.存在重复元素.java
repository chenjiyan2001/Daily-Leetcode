class Solution {
    // 1. O(n) t:5ms(88%) O(n) m:49.5M(77%) 哈希表
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<Integer>();
        for (int num : nums) {
            if (!set.add(num)) return true;
        }
        return false;
    }
}