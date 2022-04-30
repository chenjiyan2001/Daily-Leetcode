class Solution:
    # 1. O(n) t:36ms(89%) O(1) m:16M(12%) 数学
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        maximum, minimum = max(nums), min(nums)
        return maximum - minimum - 2 * k if maximum - minimum >= 2 * k else 0