class Solution:
    # 1. O(n) t:100ms(33%) O(1) m:17.2M(50%) 迭代
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None: return TreeNode(val)
        node = root
        while node:
            if node.val < val:
                if node.right is None:
                    node.right = TreeNode(val)
                    break
                node = node.right
            else:
                if node.left is None:
                    node.left = TreeNode(val)
                    break
                node = node.left
        return root