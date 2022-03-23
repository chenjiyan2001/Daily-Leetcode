class Solution:
    # [题解]1.O(log^2n) t:48ms(5%) O(1) m:14.9M(52%) 字典树模拟
    def getSteps(self, cur, n):
        steps, first, last = 0, cur, cur
        while first <= n:
            steps += min(last, n) - first + 1
            first *= 10
            last = last * 10 + 9
        return steps

    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        k -= 1
        while k:
            steps = getSteps(cur, n)
            if steps <= k:
                k -= steps
                cur += 1
            else:
                k -= 1
                cur *= 10
        return cur