class Solution:
    # 1. O(n) t:44ms(22%) O(n) m:15M(41%) 栈
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for i in s:
            if i in d:
                if not stack or d[i] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return not stack