class Solution {
    // 1. O(n) t:0ms O(1) m:36.2M(53%)
    public int removePalindromeSub(String s) {
        int n = s.length();
        for (int i = 0; i <= n / 2; i++){
            if (s.charAt(i) != s.charAt(n - i - 1)) return 2;
        }
        return 1;
    }
}