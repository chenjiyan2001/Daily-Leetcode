class Solution:
    # O(1) t:36ms(49%) m:14.9M(61%)
    def totalMoney(self, n: int) -> int:
        day = n % 7
        week = n // 7
        return 28 * week + week*(week+1)//2*7 + day*(day+1+2*week)//2