class Solution {
public:
    // 1. O(log|n|) t:0ms(100%) O(1) m:5.8M(75%)
    string convertToBase7(int num) {
        if (num == 0) return "0";
        bool flag = num < 0;
        if (flag) num = -num;
        string ans;
        while (num > 0){
            ans.push_back(num % 7 + '0');
            num /= 7;
        }
        if (flag) ans.push_back('-');
        reverse(ans.begin(), ans.end());
        return ans;
    }
};