class Solution:
    # 1. O(n) t:156ms(28%) O(1) m:19.1M(74%) 模拟
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        diff = (m+n) * mean - sum(rolls)
        base = diff // n
        ad = diff - base * n
        ans = []
        maxNum = (base + ad // n) if ad / n - int(ad / n) < 1e-6 else (base + ad // n + 1)
        if maxNum > 6 or base <= 0: return ans
        ans = [base for i in range(n)]
        for i in range(maxNum - base):
            for j in range(n):
                ans[j] += 1
                ad -= 1
                if ad == 0:
                    return ans
        return ans
    
    # [题解]2. O(n) t:72ms(92%) O(1) m:19.6M(24%) 数学
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        diff = (m+n) * mean - sum(rolls)
        if not n <= diff <= 6*n: return []
        q, r = divmod(diff, n)
        return [q+1] * r + [q] * (n-r)