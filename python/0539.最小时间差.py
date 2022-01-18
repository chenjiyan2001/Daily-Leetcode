class Solution:
    # # 1. O(nlogn) t:56ms(19%) O(logn) m:23.7M(5%) 排序1
    # def findMinDifference(self, timePoints: List[str]) -> int:
    #     times = list(map(lambda t:t.split(':'), timePoints))
    #     times1 = sorted(list(map(lambda x:int(x[0])*60+int(x[1]), times)))
    #     times2 = [1440 - t for t in times1]
    #     res = [min(times1[i+1] - times1[i], times2[i] - times2[i+1]) for i in range(len(times1)-1)]
    #     res.append(times1[0] - times1[-1] + 1440)
    #     return min(res)
    
    # # 2. O(nlogn) t:52ms(36%) O(logn) m:16.4M(85%) 排序2
    # def getTime(self, a, b):
    #     a1, a2 = a.split(':')
    #     b1, b2 = b.split(':')
    #     return 60*(int(b1) - int(a1)) + int(b2) - int(a2)

    # def findMinDifference(self, timePoints: List[str]) -> int:
    #     timePoints.sort()
    #     times = [self.getTime(timePoints[i], timePoints[i+1]) for i in range(len(timePoints)-1)]
    #     times.append(self.getTime(timePoints[-1], timePoints[0]) + 1440)
    #     return min(times)
    
    # [题解]3. O(min(n, C)logmin(n, C)) t:36ms(87%) O(logmin(n, C)) 排序2+鸽巢/抽屉
    def getTime(self, a, b):
        a1, a2 = a.split(':')
        b1, b2 = b.split(':')
        return 60*(int(b1) - int(a1)) + int(b2) - int(a2)

    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) >= 1440:
            return 0
        timePoints.sort()
        times = [self.getTime(timePoints[i], timePoints[i+1]) for i in range(len(timePoints)-1)]
        times.append(self.getTime(timePoints[-1], timePoints[0]) + 1440)
        return min(times)