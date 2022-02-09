class Solution {
    // [题解]1. O(n) t:4ms(75%) O(n) m:40.4M(11%)
    public int countKDifference(int[] nums, int k) {
        Map<Integer, Integer> cnts = new HashMap<Integer, Integer>();
        int ans = 0;
        for (int i: nums){
            ans += cnts.getOrDefault(i - k, 0) + cnts.getOrDefault(i + k, 0);
            cnts.put(i, cnts.getOrDefault(i, 0) + 1);
        }
        return ans;
    }
}