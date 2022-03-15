class Solution:
    # 1. O(m+n) t:48ms(88%) O(S) m:15M(93%) 计数
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = Counter(magazine)
        for s in ransomNote:
            if d[s] > 0: d[s] -= 1
            else: return False
        return True