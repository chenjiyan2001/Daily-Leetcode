class Solution:
    # 1. O(n*2^n) t:1068ms(36%) O(1) m:14.9M(92%) 暴力
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr = reduce(lambda a, b: a | b, nums)
        n = len(nums)
        cnt = 0
        for i in range(1, n + 1):
            for comb in combinations(nums, i):
                if reduce(lambda a, b: a | b, comb) == maxOr:
                    cnt += 1
        return cnt
    
    # [题解]2. O(2^n) t:476ms(62%) O(n) m:15.1M(53%) DFS
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr = reduce(lambda a, b: a | b, nums)
        n = len(nums)
        ans = 0
        def dfs(idx, val):
            nonlocal ans
            if idx == n: 
                ans += int(val == maxOr)
                return
            dfs(idx + 1, val | nums[idx])
            dfs(idx + 1, val)
        dfs(0, 0)
        return ans
    
    # [题解]3. O(2^n) t:144ms(85%) O(1) m:15.1M(57%) DFS+剪枝
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr = reduce(lambda a, b: a | b, nums)
        n =len(nums)
        ans = 0

        def dfs(idx, val):
            nonlocal ans
            if idx == n:
                ans += int(val == maxOr)
                return
            nxt = val | nums[idx]
            if nxt == maxOr:
                dfs(idx + 1, val) 
                ans += (1 << (n - 1 - idx))  
            else:
                dfs(idx + 1, val)
                dfs(idx + 1, nxt)
        
        dfs(0, 0)
        return ans
