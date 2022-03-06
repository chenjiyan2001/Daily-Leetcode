class Solution:
    # [题解]1. O(n) t:308ms(13%) O(n) m:32.9M(19%)
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        l, r = [0] * n, [0] * n
        for i in range(1, n):
            if security[i - 1] >= security[i]:
                l[i] = l[i - 1] + 1
            if security[n - i - 1] <= security[n - i]:
                r[n - i - 1] = r[n - i] + 1   
        ans = [i for i in range(n) if l[i] >= time and r[i] >= time]
        return ans