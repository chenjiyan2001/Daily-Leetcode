class Solution:
    # 1. O(n) t:52ms(63%) O(n) m:16.8M(55%) 迭代
    def postorder(self, root: 'Node') -> List[int]:
        if root is None: return []
        stack, ans = root.children, [root.val]
        while stack:
            node = stack.pop()
            if node.children:
                stack.extend(node.children)
            ans.append(node.val)
        return ans[::-1]
    
    # 2. O(n) t:56ms(39%) m:16.9M(40%) 递归
    def postorder(self, root: 'Node') -> List[int]:
        if root is None: return []
        ans = []
        def dfs(node):
            nonlocal ans
            for n in node.children:
                dfs(n)
            ans.append(node.val)
        
        dfs(root)
        return ans