class Solution:
    # [题解]1. O(n + m) t:324ms(63%) O(n) m:44.5M(28%)
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n, m = len(s), len(queries)
        l, r, sum, ans = [0] * n, [0] * n, [0] * (n + 1), [0] * m
        p, q = -1, -1
        for i in range(n):
            if s[i] == '|': p = i
            if s[n - 1 - i] == '|': q = n - 1 - i
            l[i], r[n - i - 1] = p, q
            sum[i + 1] += sum[i] + (1 if s[i] == '*' else 0)
        for j in range(m):
            b, e = queries[j]
            c, d = r[b], l[e]
            if c != -1 and c <= d:
                ans[j] = sum[d + 1] - sum[c]
        return ans