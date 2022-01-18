class Solution:
    # # 1. O(nC) t:472ms O(nC) m:15M(77%) 动态规划1
    # def countVowelPermutation(self, n: int) -> int:
    #     if n == 1: return 5
    #     comb = {
    #         'a':['e'],
    #         'e':['a', 'i'],
    #         'i':['a', 'e', 'o', 'u'],
    #         'o':['i', 'u'],
    #         'u':['a']
    #     }
    #     cnt = {i:1 for i in 'aeiou'}
    #     mu = 1e9 + 7
    #     for i in range(n-1):
    #         tmp = {i:0 for i in 'aeiou'}
    #         for k, v in cnt.items():
    #             for j in comb[k]:
    #                 tmp[j] = int(tmp[j] + v % mu)
    #         cnt = tmp
    #     res = sum(cnt.values())
    #     return int(res % mu)
    
    # # [题解]2. O(nC) t:88ms O(nC) m:15M(81%) 动态规划2
    # def countVowelPermutation(self, n: int) -> int:
    #     dp, mu = (1, 1, 1, 1, 1), 1000000007
    #     for i in range(n-1):
    #         dp = (
    #             (dp[1] + dp[2] + dp[4])% mu,
    #             (dp[0] + dp[2]) % mu,
    #             (dp[1] + dp[3]) % mu,
    #             dp[2],
    #             (dp[2] + dp[3]) % mu
    #         )
    #     return sum(dp) % mu

    # [题解]3. O(C^3logn) t:84ms O(C^2) m:32.1M(24%) 矩阵快速幂
    def countVowelPermutation(self, n: int) -> int:
        import numpy as np
        MOD = int(1e9) + 7
        ans = np.array([1, 1, 1, 1, 1])
        mat = np.array([
            [0, 1, 1, 0, 1], 
            [1, 0, 1, 0, 0], 
            [0, 1, 0, 1, 0], 
            [0, 0, 1, 0, 0], 
            [0, 0, 1, 1, 0]])
        n -= 1
        while n:
            if n & 1:
                ans = ans @ mat % MOD
            mat = mat @ mat % MOD
            n >>= 1
        return int(ans.sum()) % MOD