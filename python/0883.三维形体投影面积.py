class Solution:
    # 1. O(n) t:40ms(80%) O(1) m:15.2M(9%) 遍历
    def projectionArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            ans += max(grid[i])
            for j in range(n):
                if grid[i][j]:
                    ans += 1
        for i in range(n):
            cur = 0
            for j in range(m):
                cur = max(cur, grid[j][i])
            ans += cur
        return ans