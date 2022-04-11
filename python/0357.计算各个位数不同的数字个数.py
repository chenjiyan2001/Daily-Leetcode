class Solution:
    # [题解]1. O(n) t:32ms(90%) O(1) m:14.8M(80%) 数学
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n < 2: return 10 ** n
        ans, cur = 10, 9
        for i in range(n - 1):
            cur *= 9 - i
            ans += cur
        return ans
    
    