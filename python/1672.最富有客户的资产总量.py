class Solution:
    # 1. O(n) t:28ms(97%) O(1) m:14.9M(90%) 模拟
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(list(map(sum, accounts)))