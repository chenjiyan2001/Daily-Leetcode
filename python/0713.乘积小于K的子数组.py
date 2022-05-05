class Solution:
    # [题解]O(n) t:140ms(82%) O(1) m:17.1M(49%) 双指针
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i, ans, cur = 0, 0, 1
        for j, num in enumerate(nums):
            cur *= num
            while i <= j and cur >= k:
                cur //= nums[i]
                i += 1
            ans += j - i + 1
        return ans