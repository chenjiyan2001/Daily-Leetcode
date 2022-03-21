class Solution:
    # [题解]1. O(n) t:44ms(11%) O(h) m:14.9M(60%) 递归
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 节点为空时返回
        if root is None: return None
        # 交换左右子树
        root.left,root.right = root.right,root.left
        # 递归交换左右子树
        self.invertTree(root.left)
        self.invertTree(root.right)
        # 返回时说明已经交换完毕
        return root