class Solution:
    # [题解]1. O(nlogn) t:48ms(67%) O(logn) m:17.9M(37%) 排序
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        ans = []
        for i in range(n):
            if not ans or ans[-1][1] < intervals[i][0]:
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
        return ans