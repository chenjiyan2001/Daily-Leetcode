class Solution:
    # 1. O(n) t:44ms(98%) O(1) m:18.6M(94%) 模拟
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        cur = 1
        cnt = 1
        while cnt <= n:
            while cur * 10 <= n:
                ans.append(cur)
                cur *= 10
                cnt += 1
            else:
                diff = min(n - cur, 9 - cur % 10)
                for i in range(cur, cur + diff + 1):
                    ans.append(i)
                    cnt += 1
            while (cur // 10 + 1) % 10 == 0:
                cur //= 10
            cur = cur // 10 + 1
        return ans