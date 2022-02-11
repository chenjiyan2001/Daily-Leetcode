class Solution:
    # 1. O(nlogn) t:40ms(83%) O(logn) m:15M(59%)
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1: return 0
        nums.sort()
        return min(nums[i + k - 1] - nums[i] for i in range(n - k + 1))