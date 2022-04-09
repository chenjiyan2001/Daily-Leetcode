class Solution:
    # 1. O(nlogn) t:44ms(84%) O(1) m:16M(48%)
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            ans.append(i.bit_count())
        return ans
    
    # 2. O(n) t:64ms(37%) O(1) m:16M(48%) 动态规划
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        base = 1
        for i in range(1, n+1):
            if i == base * 2:
                base *= 2
            ans[i] = ans[i - base] + 1
        return ans