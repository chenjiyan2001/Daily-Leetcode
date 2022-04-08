class Solution:
    # 1. O(n) t:40ms(30%) m:15M(36%) 哈希+模拟
    def rotateString(self, s: str, goal: str) -> bool:
        k = hash(goal)
        n = len(s)
        cnt = 0
        while cnt < n:
            s = s[1:] + s[0]
            if hash(s) == k:
                return True
            cnt += 1
        return False
    
    # [题解]2. O(n) t:36ms(60%) O(n) m:15M(45%) 搜索子字符串
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s
