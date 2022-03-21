class Solution:
    # 1. O(n) t:48ms(50%) O(h) m:16.3M(5%) 迭代
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == targetSum and node.left is None and node.right is None:
                return True
            if node.left:
                node.left.val += node.val
                stack.append(node.left)
            if node.right:
                node.right.val += node.val
                stack.append(node.right)
        return False
    
    # 2. O(n) t:44ms(74%) m:16.sM(32%) 递归
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False
        num = targetSum - root.val
        if num == 0 and root.left is None and root.right is None: return True
        return self.hasPathSum(root.left, num) or self.hasPathSum(root.right, num)
