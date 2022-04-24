class Solution:
    # 1. O(logn) t:36ms(71%) O(1) m:14.9M(56%) 位运算
    def binaryGap(self, n: int) -> int:
        ans, cnt, flag = 0, 0, 0
        while n > 0:
            if n & 1:
                if flag:
                    ans = max(ans, cnt)
                    cnt = 1
                else:
                    cnt = 1
                    flag = 1
            else:
                cnt += 1
            n >>= 1
        return ans