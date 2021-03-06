class Solution:
    # 1. O(n) t:172ms(51%) O(1) m:17.8M(69%) 两次遍历
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans, cur = 0, 1
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1] and i % 2 == 0:
                cur += 1
            elif arr[i] > arr[i+1] and i % 2 == 1:
                cur += 1
            else:
                ans = max(ans, cur)
                cur = 1
        ans = max(ans, cur)
        cur = 1
        for i in range(len(arr) - 1):
            if arr[i] < arr[i+1] and i % 2 == 1:
                cur += 1
            elif arr[i] > arr[i+1] and i % 2 == 0:
                cur += 1
            else:
                ans = max(ans, cur)
                cur = 1
        ans = max(ans, cur)
        return ans 
    
    # 2. O(n) t:128ms(82%) O(1) m:17.9M(61%) 一次遍历
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans, cur1, cur2 = 0, 1, 1
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                if i % 2 == 0:
                    cur1 += 1
                    ans = max(ans, cur2)
                    cur2 = 1
                else:
                    ans = max(ans, cur1)
                    cur1 = 1
                    cur2 += 1
            elif arr[i] > arr[i+1]:
                if i % 2 == 1:
                    cur1 += 1
                    ans = max(ans, cur2)
                    cur2 = 1
                else:
                    ans = max(ans, cur1)
                    cur1 = 1
                    cur2 += 1
            else:
                ans = max(ans, cur1, cur2)
                cur1, cur2 = 1, 1
        ans = max(ans, cur1, cur2)
        return ans 

    # [题解]3. O(n) t:192ms(34%) O(n) m:20.2M(5%) DP
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n, ans = len(arr), 1
        dp = [[1, 1] for _ in range(n)]
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                dp[i][0] = dp[i-1][1] + 1
            elif arr[i] < arr[i-1]:
                dp[i][1] = dp[i-1][0] + 1
            ans = max(ans, dp[i][0], dp[i][1])
        return ans

    # [题解]4. O(n) t:200ms(24%) O(1) m:17.8M(74%) DP+奇偶滚动
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n, ans = len(arr), 1
        dp = [[1, 1] for _ in range(2)]
        for i in range(1, n):
            dp[i % 2][0] = dp[i % 2][1] = 1
            if arr[i] > arr[i-1]:
                dp[i % 2][0] = dp[(i - 1) % 2][1] + 1
            elif arr[i] < arr[i-1]:
                dp[i % 2][1] = dp[(i - 1) % 2][0] + 1
            ans = max(ans, dp[i % 2][0], dp[i % 2][1])
        return ans
    
    # [题解]5. O(n) t:160ms(59%) O(1) m:17.8M(82%) DP+维度消除
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n, ans = len(arr), 1
        dp = [1, 1]
        for i in range(1, n):
            a, b = dp
            dp[0] = (b + 1) if arr[i] > arr[i-1] else 1
            dp[1] = (a + 1) if arr[i] < arr[i-1] else 1
            ans = max(ans, dp[0], dp[1])
        return ans