class Solution {
public:
    // [题解]1. O(m + n) t:372(73%) O(n) m:141.7M(27%) 前缀和
    vector<int> platesBetweenCandles(string s, vector<vector<int>>& queries) {
        int n = s.length();
        vector<int> l(n), r(n), sum(n + 1);
        for (int i = 0, j = n - 1, p = -1, q = -1; i < n; i++, j--){
            if (s[i] == '|') p = i;
            if (s[j] == '|') q = j;
            l[i] = p; r[j] = q;
            sum[i + 1] = sum[i] + (s[i] == '*' ? 1 : 0);
        }
        vector<int> ans;
        for (auto& query : queries){
            int a = query[0], b = query[1];
            int c = r[a], d = l[b];
            if (c != -1 && c <= d){
                ans.push_back(sum[d + 1] - sum[c]);
            }else{
                ans.push_back(0);
            }
        }
        return ans;
    }
};