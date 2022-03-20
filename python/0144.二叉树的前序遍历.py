class Solution:
    # 1. O(n) t:40ms(30%) O(n) m:14.9M(47%) 迭代
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ans