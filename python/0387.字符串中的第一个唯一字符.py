class Solution:
    # 1. O(n) t:96ms(60%) O(m) m:14.9M(98%) 哈希
    def firstUniqChar(self, s: str) -> int:
        d = Counter(s)
        for idx, i in enumerate(s):
            if d[i] == 1: return idx
        return -1