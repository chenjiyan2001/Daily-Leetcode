class Solution:
    # 1.O(n) t:52ms(80%) O(1) m:15M(87%) 模拟
    def convert(self, s: str, numRows: int) -> str:
        m, n = numRows * 2 - 2, len(s)
        if n == 1 or numRows == 1: return s
        ans, idx = '', 0
        while idx < n:
            ans += s[idx]
            idx += m
        for i in range(1, numRows - 1):
            idx = i
            while idx < n:
                ans += s[idx]
                if idx - i + m - i < n:
                    ans += s[idx - i + m - i]
                idx += m
        idx = numRows - 1
        while idx < n:
            ans += s[idx]
            idx += m
        return ans