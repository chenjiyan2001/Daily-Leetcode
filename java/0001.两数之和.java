class Solution {
    // 1. O(n) t:1ms(100%) m:39.8M(19%) Hash
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            int x = nums[i];
            if (map.containsKey(target - x)){
                return new int[]{map.get(target - x), i};
            }
            map.put(x, i);
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}
