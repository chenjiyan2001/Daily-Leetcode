class Solution:
    # 1. O(log|n|) t:44ms(7%) O(1) m:14.9M(77%)
    def convertToBase7(self, num: int) -> str:
        if num == 0: return '0'
        flag = 1 if num < 0 else 0
        num = abs(num)
        ans = ''
        while num > 0:
            ans += str(num % 7)
            num //= 7
        return ('-' if flag else '') + ans[::-1]