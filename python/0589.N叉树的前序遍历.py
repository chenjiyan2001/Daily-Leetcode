class Solution:
    # 1. O(n) t:68ms(7%) O(n) m:16.9M(44%) 迭代
    def preorder(self, root: 'Node') -> List[int]:
        stack, ans = [root], []
        while stack:
            node = stack.pop(0)
            if node:
                ans.append(node.val)
                stack = node.children + stack
            else:
                continue
        return ans
    
    # [题解]2. O(n) t:68ms(7%) O(1) m:17.3M(5%) 递归
    def preorder(self, root: 'Node') -> List[int]:
        return ([root.val] + [x for node in root.children for x in self.preorder(node)]) if root else []
