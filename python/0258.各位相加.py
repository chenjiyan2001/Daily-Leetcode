class Solution:
    # # 1. O(lognum) t:48ms(6%) O(1) m:14.8M(80%) 模拟
    # def addDigits(self, num: int) -> int:
    #     while num >= 10:
    #         sum = 0
    #         while num > 0:
    #             sum += num % 10
    #             num //= 10
    #         num = sum
    #     return num

    # [题解]2. O(1) t:44ms O(1) m:14.8M(91%) 数学
    def addDigits(self, num: int) -> int:
        if num == 0:
            ans = 0
        elif num % 9 == 0:
            ans = 9
        else:
            ans = num % 9
        return ans