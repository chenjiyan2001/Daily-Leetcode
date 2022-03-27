class Solution:
    # 1. O(n^2) t:36ms(61%) O(1) m:14.9M(76%) 递推
    def getRow(self, rowIndex: int) -> List[int]:
        base = [1]
        for i in range(rowIndex):
            base = [a+b for a,b in zip(base+[0], [0]+base)]
        return base
    
    # [题解]2. O(n) t:32ms(83%) O(1) m:14.9M(68%) 数学
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for i in range(rowIndex):
            ans.append(ans[i] * (rowIndex - i) // (i + 1))
        return ans