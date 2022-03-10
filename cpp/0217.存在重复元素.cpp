class Solution {
public:
    // 1. O(n) t:64ms(83%) O(n) m:50.1M(44%) 哈希表
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> s;
        for (int x: nums) {
            if (s.find(x) != s.end()) return true;
            s.insert(x);
        }
        return false;
    }
};