class Solution:
    # 1. O(n) t:44ms(33%) O(c) m:15.5M(74%)
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c: return mat
        ans, tmp, cnt = [], [], 0
        for i in range(m):
            for j in range(n):
                tmp.append(mat[i][j])
                cnt += 1
                if cnt == c:
                    ans.append(tmp)
                    tmp, cnt = [], 0
        return ans