class Solution:
    # [题解]1. O(n) t:32ms(81%) m:14.9M(44%) 迭代法
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, ans = [], []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
            root = root.right
        return ans
    
    