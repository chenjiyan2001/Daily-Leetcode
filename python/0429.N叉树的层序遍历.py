class Solution:
    # 1. O(n) t:48ms(93%) O(n) m:16.9M(52%) 层序遍历
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        queue = [root]
        ans = []
        while queue:
            nxt = []
            vals = []
            for node in queue:
                nxt.extend(node.children)
                vals.append(node.val)
            queue = nxt
            ans.append(vals)
        return ans