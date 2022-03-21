class Solution:
    # [题解]1. O(n) t:80ms(56%) O(n) m:19.4M(58%) 哈希+树的搜索
    def __init__(self):
       self.s = set()
   
   def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
       if root is None: return False
       if (k - root.val) in self.s: return True
       self.s.add(root.val)
       return self.findTarget(root.left, k) or self.findTarget(root.right, k)

    # [题解]2. O(n) t:100ms(22%) O(n) m:20.9M(38%) 双指针+BFS中序遍历+迭代器
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def in_order(node):
            if node:
                yield from in_order(node.left)
                yield node.val
                yield from in_order(node.right)
        
        def in_order_reverse(node):
            if node:
                yield from in_order_reverse(node.right)
                yield node.val
                yield from in_order_reverse(node.left)

        left_gen, right_gen = in_order(root), in_order_reverse(root)
        left, right = next(left_gen), next(right_gen)
        while left < right:
            if left + right < k:
                left = next(left_gen)
            elif left + right > k:
                right = next(right_gen)
            else:
                return True
        return False