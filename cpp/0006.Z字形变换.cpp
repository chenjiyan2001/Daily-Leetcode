class Solution {
public:
    // 1. O(n) t:8ms(77%) O(1) m:8.1M(78%)
    string convert(string s, int numRows) {
        int m = numRows * 2 - 2, n = s.length();
        if (n == 1 || numRows == 1) return s;
        int idx = 0;
        string ans;
        while (idx < n){
            ans += s[idx];
            idx += m;
        }
        for (int i = 1; i < numRows - 1; i++){
            idx = i;
            while (idx < n){
                ans += s[idx];
                if (idx - i + m - i < n)
                    ans += s[idx - i + m - i];
                idx += m;
            }
        }
        idx = numRows - 1;
        while (idx < n){
            ans += s[idx];
            idx += m;
        }
        return ans;
    }
};