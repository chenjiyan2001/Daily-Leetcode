class Solution {
public:
    // [题解]1. O(n) t:8ms(92%) O(n) m:10.4M(50%)
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashtable;
        for (int i = 0; i < nums.size(); ++i) {
            auto it = hashtable.find(target - nums[i]);
            if (it != hashtable.end()) return {it->second, i};
            hashtable[nums[i]] = i;
        }
        return {};
    }
};