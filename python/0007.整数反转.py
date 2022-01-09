class Solution:
    # # 1. t:36ms(54%) m:14.9M(54%) array
    # def reverse(self, x: int) -> int:
    #     border = 2**31
    #     x = str(x)[::-1]
    #     if x.endswith('-'):
    #         x = x[-1] + x[:-1]
    #     x = int(x)
    #     x = x if -border <= x and x <= border-1 else 0
    #     return x

    # 2. O(log|x|) t:32ms(80%) m:14.9M(62%) stack
    def reverse(self, x: int) -> int:
        border = 2**31
        rev = 0
        while x != 0:
            digit = x % 10
            digit = (digit - 10) if x < 0 and digit > 0 else digit
            x = (x - digit) // 10
            rev = rev * 10 + digit
        rev = rev if -border <= rev and rev <= border-1 else 0
        return rev