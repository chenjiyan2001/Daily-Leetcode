class Solution {
public:
    // [题解]1. O(n) t:12ms(99%) O(n) m:10.3M(29%)
    long long subArrayRanges(vector<int>& nums) {
        stack<int> minStack, maxStack;
        int n = nums.size();
        long ans = 0;
        for (int i = 0; i <= n; i++){
            while (!minStack.empty() && (i == n || nums[minStack.top()] > nums[i])){
                int j = minStack.top();
                minStack.pop();
                ans -= (long)nums[j] * (i - j) * (j - (minStack.empty() ? -1 : minStack.top()));
            }
            minStack.push(i);
        }

        for (int i = 0; i <= n; i++){
            while (!maxStack.empty() && (i == n || nums[maxStack.top()] < nums[i])){
                int j = maxStack.top();
                maxStack.pop();
                ans += (long)nums[j] * (i - j) * (j - (maxStack.empty() ? -1 : maxStack.top()));
            }
            maxStack.push(i);
        }

        return ans;
    }
};