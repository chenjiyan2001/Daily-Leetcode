class Solution:
    # 1. O(n) t:28ms(85%) O(n) m:15.1M(10%)
    def removePalindromeSub(self, s: str) -> int:
        return 1 if s == s[::-1] else 2
    
    # # 2. O(n) t:32ms(65%) O(1) m:15.1M(6%)
    # def removePalindromeSub(self, s: str) -> int:
    #     for i in range(len(s)//2):
    #         if s[i] != s[len(s)-1-i]:
    #             return 2
    #     return 1