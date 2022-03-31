class Solution:
    # 1. O(nlogL) t:36ms(97%) O(1) m:14.9M(77%) 模拟
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right+1):
            num = i
            while num > 0:
                if num % 10 == 0 or i % (num % 10) != 0:
                    break
                num //= 10
            if num == 0:
                ans.append(i)
        return ans