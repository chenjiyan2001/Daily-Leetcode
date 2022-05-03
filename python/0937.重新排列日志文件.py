class Solution:
    # [题解]1. O(nlogn) t:40ms(49%) O(1) m:15.2M(37%) 自定义排序
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def logSort(log):
            a, b = log.split(' ', 1)
            return (0, b, a) if b[0].isalpha() else (1,)
        logs.sort(key=logSort)
        return logs
