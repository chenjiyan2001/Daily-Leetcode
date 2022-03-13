class Solution:
    # 1. O(n) t:72ms(23%) O(1) m:15.1M(90%)
    def validUtf8(self, data: List[int]) -> bool:
        flag, cnt = True, 0
        for d in data:
            if int('11110000', 2) <= d <= int('11110111', 2) and cnt == 0:
                cnt = 3
            elif int('11100000', 2) <= d <= int('11101111', 2) and cnt == 0:
                cnt = 2
            elif int('11000000', 2) <= d <= int('11011111', 2) and cnt == 0:
                cnt = 1
            elif int('10000000', 2) <= d <= int('10111111', 2) and cnt > 0:
                cnt -= 1
            elif int('00000000', 2) <= d <= int('01111111', 2) and cnt == 0:
                continue
            else:
                flag = False
                break
        if cnt > 0: flag = False
        return flag