class Solution:
    # 1. O(mn) t:48ms(33%) O(1) m:15.6M(5%)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        r, c = [], []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    r.append(i)
                    c.append(j)
        for i in set(r):
            matrix[i] = [0] * n
        for i in range(m):
            for j in set(c):
                matrix[i][j] = 0