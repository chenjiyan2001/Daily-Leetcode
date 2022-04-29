class Solution:
    # [题解]1. O(n^2logn) t:200ms(87%) O(logn) m:15.8M(47%) 递归遍历
    def construct(self, grid) -> 'Node':
        n = len(grid)

        def inorder(x, y, l):
            cur = grid[x][y]
            for i in range(l):
                for j in range(l):
                    if cur != grid[x + i][y + j]:
                        break
                if j != l - 1:
                    break
            if i == l - 1 and j == l - 1:
                return Node(cur, True)
            else:
                nl = l >> 1
                return Node(
                    cur, 
                    False, 
                    inorder(x, y, nl),
                    inorder(x, y + nl, nl),
                    inorder(x + nl, y, nl),
                    inorder(x + nl, y + nl, nl)
                    )

        ans = inorder(0, 0, n)
        return ans
    # [题解]1. O(n^2+logn) t:200ms(87%) O(n^2) m:16.1M(12%) 前缀和优化
    def construct(self, grid) -> 'Node':
        n = len(grid)
        presum = [[0] * (n + 1) for _ in range(n + 1)]
        # 二维前缀和
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                presum[i][j] += presum[i][j+1] + presum[i+1][j] - presum[i+1][j+1] + grid[i][j]

        def inorder(x, y, l):
            cur = presum[x][y] - presum[x+l][y] - presum[x][y+l] + presum[x+l][y+l]
            if cur == 0 or cur == l ** 2:
                return Node(bool(cur), True)
            else:
                nl = l >> 1
                return Node(
                    cur, 
                    False, 
                    inorder(x, y, nl),
                    inorder(x, y + nl, nl),
                    inorder(x + nl, y, nl),
                    inorder(x + nl, y + nl, nl)
                    )

        ans = inorder(0, 0, n)
        return ans