class Solution {
    // 1. O(n) t:2ms(99%) O(1) m:41.6M(51%)
    public String convert(String s, int numRows) {
        int m = numRows * 2 - 2, n = s.length();
        if (n == 1 || numRows == 1) return s;
        int idx = 0;
        StringBuilder ans = new StringBuilder();
        while (idx < n){
            ans.append(s.charAt(idx));
            idx += m;
        }
        for (int i = 1; i < numRows - 1; i++){
            idx = i;
            while (idx < n){
                ans.append(s.charAt(idx));
                if (idx - i + m - i < n)
                    ans.append(s.charAt(idx - i + m - i));
                idx += m;
            }
        }
        idx = numRows - 1;
        while (idx < n){
            ans.append(s.charAt(idx));
            idx += m;
        }
        return ans.toString();
    }
}