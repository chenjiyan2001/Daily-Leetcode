class Solution {
    // 1. O(1) t:0ms(100%) O(1) m:39M(26%) 脑筋急转弯
    public int findLUSlength(String a, String b) {
        return !a.equals(b) ? Math.max(a.length(), b.length()) : -1;
    }
}