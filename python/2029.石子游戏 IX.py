class Solution:
    # [题解]1. O(n) t:148ms O(1) m:25.3M(24%)
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnts = {i:0 for i in range(3)}
        for s in stones:
            cnts[s % 3] += 1
        flag = cnts[0] & 1
        if flag:
            return cnts[1] - cnts[2] > 2 or cnts[2] - cnts[1] > 2
        else:
            return cnts[1] >= 1 and cnts[2] >= 1