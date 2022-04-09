class Solution:
    # 1. O(n) t:236ms(28%) O(1) m:24.1M(92%) 双指针
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n - 1
        ans = 0
        while i < j:
            ans = max(ans, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans