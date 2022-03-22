class Solution:
    # 1. O(n) t:76ms(51%) O(1) m:17.1M(37%) 迭代
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            n = root.val
            if n == val:
                return root
            elif n < val:
                root = root.right
            else:
                root = root.left
        return None
    
    # 2. O(n) t:68ms(85%) O(1) m:17M(61%) 递归
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        return root if root is None or root.val == val else (self.searchBST(root.left, val) if root.val > val else self.searchBST(root.right, val))
