class Solution:
    # [题解]1. O(n) t:108ms(83%) O(n) m:25.3M(13%) 动态规划
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        d = defaultdict(int)
        for num in arr:
            d[num] = d[num - difference] + 1
        return max(d.values())