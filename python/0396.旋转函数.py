class Solution:
    # 1. O(n) t:412ms(16%) O(1) m:21.8M(77%) 前缀和+滑动窗口
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        sumNum = sum(nums)
        curSum = sum(i * k for i, k in enumerate(nums))
        ans = -inf
        for i in range(n):
            curSum += sumNum - nums[n - i - 1] * n
            ans = max(curSum, ans)
        return ans