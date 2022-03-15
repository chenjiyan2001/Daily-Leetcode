class Solution:
    # 1. O(n) t:48ms(70%) O(S) m:15.2M(77%) 计数
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        cnt = Counter(s)
        for i in t:
            if cnt[i] == 0: return False
            cnt[i] -= 1
        return True