class Solution {
public:
    // [题解]1. O(n) t:116ms O(n) m:87.6M(19%)
    vector<int> goodDaysToRobBank(vector<int>& security, int time) {
        int n = security.size();
        vector<int> l(n);
        vector<int> r(n);
        for (int i = 1; i < n; i++){
            if (security[i - 1] >= security[i]){
                l[i] = l[i - 1] + 1;
            }
            if (security[n - i - 1] <= security[n - i]){
                r[n - i - 1] = r[n - i] + 1;
            }
        }

        vector<int> ans;
        for (int i = 0; i < n; i++){
            if (l[i] >= time && r[i] >= time){
                ans.emplace_back(i);
            }
        }
        return ans;
    }
};