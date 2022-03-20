class Solution:
    # [题解]1. O(n) t:28ms(94%) O(n) m:14.9M(62%) 迭代
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, ans = [], []
        prev = None # 记录是否访问过右子树
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == prev: # 已访问过右子树
                ans.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right
        return ans