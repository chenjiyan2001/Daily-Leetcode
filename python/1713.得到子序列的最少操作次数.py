class Solution:
    # [题解]1. O(n+mlogm) t:352ms(26%) O(n+m) m:39M(36%) 动态规划
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        map = {v:i for i, v in enumerate(target)}
        arr = [map[i] for i in arr if i in map.keys()]
        dp = []
        for num in arr:
            if not dp or num > dp[-1]:
                dp.append(num)
            else:
                idx = bisect_left(dp, num)
                dp[idx] = num
        return len(target) - len(dp)