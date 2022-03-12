class Solution {
public:
    // 1. O(n) t:ms(88%) O(1) m:9.9M(64%) 双指针
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        int m = nums1.size(), n = nums2.size();
        int i = 0, j = 0, idx = 0;
        vector<int> ans;
        while (i < m && j < n) {
            if (nums1[i] == nums2[j]) {
                ans.push_back(nums1[i]);
                i++;
                j++;
                idx++;
            }else if (nums1[i] < nums2[j]) {
                i++;
            }else{
                j++;
            }
        }
        return ans; 
    }
};