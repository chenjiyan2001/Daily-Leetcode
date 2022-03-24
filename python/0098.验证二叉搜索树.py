class Solution:
    # [题解]1. O(n) t:48ms(59%) O(n) m:18M(26%) 中序遍历
    def __init__(self):
        self.pre = -inf

    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if not self.isValidBST(root.left):
            return False
        if self.pre >= root.val:
            return False
        self.pre = root.val
        return self.isValidBST(root.right)