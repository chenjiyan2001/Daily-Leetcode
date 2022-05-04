class Solution:
    # 1. O(n) t:40ms(67%) O(n) m:15.2M(16%) 数组模拟
    def findTheWinner(self, n: int, k: int) -> int:
        people = [i for i in range(1, n+1)]
        i = 0
        while n > 1:
            ni = (i + k - 1) % n
            people.pop(ni)
            i = ni
            n -= 1
        return people[0]
    
    # [题解]2. O(n) t:32ms(97%) O(1) m:15.5M(5%) 递归
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1: return n
        ans = (self.findTheWinner(n - 1, k) + k) % n
        return n if ans == 0 else ans

    # [题解]3. O(n) t:36ms(88%) O(1) m:14.9M(84%) 循环
    def findTheWinner(self, n: int, k: int) -> int:
        ans = 0
        for i in range(1, n+1):
            ans = (ans + k) % i
        return ans + 1