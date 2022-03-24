class Solution:
    # 1. O(n) t:116ms(5%) O(n) m:19M(34%) 二次遍历
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def get_route(root, p):
            Node, lst = root, []
            while Node.val != p.val:
                lst.append(Node)
                val = Node.val
                if val < p.val:
                    Node = Node.right
                else:
                    Node = Node.left
            lst.append(Node)
            return lst
        
        pRoute, qRoute = get_route(root, p), get_route(root, q)
        for u, v in zip(pRoute, qRoute):
            if u.val == v.val:
                ans = u
            else:
                break
        return ans
    
    # [题解]2. O(n) t:72ms(82%) O(1) m:19M(54%) 一次遍历
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p, q = (q, p) if q.val < p.val else (p, q)
        while True:
            if root.val < p.val:
                root = root.right
            elif root.val > q.val:
                root = root.left
            else:
                return root