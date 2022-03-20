class Solution:
    # 1. O(n) t:36ms(72%) O(n) m:15.2M(84%) 迭代
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []
        queue = deque([root, -1])
        ans = [[root.val]]
        next = []
        while len(queue) > 1:
            node = queue.popleft()
            if node == -1: 
                ans.append(next)
                queue.append(-1)
                next = []
                continue
            if node.left:
                next.append(node.left.val)
                queue.append(node.left)
            if node.right:
                next.append(node.right.val)
                queue.append(node.right)
        return ans