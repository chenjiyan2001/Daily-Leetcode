class Solution:
    # [题解]1. O(n) t:28ms(97%) O(n) m:15.1M(21%) 模拟
    def lengthLongestPath(self, input: str) -> int:
        record, ans = defaultdict(int), 0
        for line in input.split("\n"):
            level, line = sum(1 for _ in takewhile(lambda x: x == '\t', line)), line.replace("\t","")
            record[level] = len(line)
            if '.' in line:
                ans = max(ans, sum(record[i] for i in range(level + 1)) + level)
        return ans