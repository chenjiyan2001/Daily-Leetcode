class Solution {
    // [题解]1. O(n) t:11ms(97%) O(n) m:41.4M(16%)
    public long subArrayRanges(int[] nums) {
        Deque<Integer> stack = new ArrayDeque<>();
        long ans = 0;
        int n = nums.length;
        for (int i = 0; i <= n; i++){
            while (!stack.isEmpty() && (i == n || nums[stack.peekLast()] < nums[i])){
                int j = stack.pollLast();
                ans += (long)nums[j] * (i - j) * (j - (stack.isEmpty() ? -1 : stack.peekLast()));
            }
            stack.offerLast(i);
        }

        stack = new ArrayDeque<>();
        for (int i = 0; i <= n; i++){
            while (!stack.isEmpty() && (i == n || nums[stack.peekLast()] > nums[i])){
                int j = stack.pollLast();
                ans -= (long)nums[j] * (i - j) * (j - (stack.isEmpty() ? -1 : stack.peekLast()));
            }
            stack.offerLast(i);
        }
        return ans;
    }
}