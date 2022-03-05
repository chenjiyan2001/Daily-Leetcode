class Solution:
    # 1. O(1) t:28ms(88%) O(1) m:15M(45%) 脑筋急转弯
    def findLUSlength(self, a: str, b: str) -> int:
        return max(len(a), len(b)) if a != b else -1