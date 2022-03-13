class Solution:
    # 1. O(n^2) t:36ms(50%) O(1) m:15M(31%)
    def generate(self, numRows: int) -> List[List[int]]:
        ans, row = [[1]], 1
        while max(numRows - 1, 0):
            row += 1
            tmp = [1]
            numRows -= 1
            n = len(ans[-1])
            for i in range(n - 1):
                tmp.append(ans[-1][i] + ans[-1][i + 1])
            ans.append(tmp + [1])
        return ans