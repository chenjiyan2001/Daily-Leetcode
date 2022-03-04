class Solution:
    # # 1. O(n^2) t:3844ms(17%) O(1) m:15M
    # def subArrayRanges(self, nums: List[int]) -> int:
    #     ans, n = 0, len(nums)
    #     for i in range(n):
    #         maxVal, minVal = -inf, inf
    #         for j in range(i, n):
    #             maxVal = max(maxVal, nums[j])
    #             minVal = min(minVal, nums[j])
    #             ans += maxVal - minVal
    #     return ans
    
    # [题解]2. O(n) t:52ms(98%) O(n) m:14.9M(92%)
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0
        stack = []
        for i, num in enumerate(nums + [inf]):
            while stack and nums[stack[-1]] < num:
                j = stack.pop()
                ans += nums[j] * (i - j) * (j - (stack[-1] if stack else -1))
            stack.append(i)
        
        stack = []
        for i, num in enumerate(nums + [-inf]):
            while stack and nums[stack[-1]] > num:
                j = stack.pop()
                ans -= nums[j] * (i - j) * (j - (stack[-1] if stack else -1))
            stack.append(i)
        return ans