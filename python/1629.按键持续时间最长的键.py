class Solution:
    # # 1. O(nlogn) t:36ms(69%) m:15.1M(54%) 字典+排序
    # def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
    #     ans = {}
    #     b = 0
    #     for t, k in zip(releaseTimes, keysPressed):
    #         new = t - b
    #         if new > ans.get(k, 0):
    #             ans[k] = new
    #         b = t
    #     result = sorted(list(ans.items()), key=lambda x:(x[1],x[0]))
    #     return result[-1][0]

    # 2. O(n) t:44ms(18%) m:15.1M(43%) 简单思路+最小内存
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_t = releaseTimes[0]
        max_k = keysPressed[0]
        for i in range(1, len(releaseTimes)):
            t = releaseTimes[i] - releaseTimes[i-1]
            k = keysPressed[i]
            if t > max_t:
                max_t = t
                max_k = keysPressed[i]
            elif t == max_t and k > max_k:
                max_k = k
        return max_k