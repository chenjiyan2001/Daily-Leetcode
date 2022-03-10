class Solution:
    # [题解]1. O(n) t:176ms(45%) O(1) m:25.6M(62%) 动态规划
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0
        ans = nums[0]
        for num in nums:
            pre = max(pre + num, num)
            ans = max(pre, ans)
        return ans