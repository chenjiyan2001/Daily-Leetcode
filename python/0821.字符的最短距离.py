class Solution:
    # 1. O(n) t:32ms(98%) O(n) m:15.1M(36%) 预处理
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        l, r = [-1] * n, [-1] * n
        li, ri = -inf, inf
        for i in range(n):
            if s[i] == c:
                li = i
            l[i] = li
            if s[n - i - 1] == c:
                ri = n - i - 1
            r[n - i - 1] = ri
        ans = [-1] * n
        for i in range(n):
            ans[i] = min(i - l[i], r[i] - i)
        return ans