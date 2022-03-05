class Solution {
public:
    // 1. O(1) t:0ms(100%) O(1) m:6M(58%) 脑筋急转弯
    int findLUSlength(string a, string b) {
        return a != b ? max(a.length(), b.length()) : -1;
    }
};