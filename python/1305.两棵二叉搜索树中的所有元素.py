class Solution:
    # 1. O(m+n) t:320ms(43%) O(1) m:24.4M(5%) 中序遍历+归并
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(root, res):
            if root:
                dfs(root.left, res)
                res.append(root.val)
                dfs(root.right, res)
        
        nums1, nums2 = [], []
        dfs(root1, nums1), dfs(root2, nums2)
        ans, idx1, idx2 = [], 0, 0
        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] <= nums2[idx2]:
                ans.append(nums1[idx1])
                idx1 += 1
            else:
                ans.append(nums2[idx2])
                idx2 += 1
        return ans + nums1[idx1:] + nums2[idx2:]

    # [题解]2. O(m+n) t:3932ms(5%) O(1) m:25.8M(5%) 中序遍历(迭代器写法)+归并
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(root):
            if root:
                yield from dfs(root.left)
                yield root.val
                yield from dfs(root.right)
        
        gen1, gen2 = dfs(root1), dfs(root2)
        a, b = next(gen1, None), next(gen2, None)
        ans = []
        while a is not None and b is not None:
            if a < b:
                ans.append(a)
                a = next(gen1, None)
            else:
                ans.append(b)
                b = next(gen2, None)
        if a is not None:
            ans.append(a)
        if b is not None:
            ans.append(b)
        ans.extend(chain(gen1, gen2))
        return ans