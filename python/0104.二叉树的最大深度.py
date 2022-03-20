class Solution:
    # 1. O(n) t:52ms(20%) O(n) m:16.3M(80%) 迭代
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        maxd = 0
        stack = [(root, 1)]
        while stack:
            node, d = stack.pop()
            maxd = max(maxd, d)
            if node.left:
                stack.append((node.left, d + 1))
            if node.right:
                stack.append((node.right, d + 1))
        return maxd