class Solution:
    # [题解]1. O(n) t:532ms(80%) m:120.3M(44%) DFS
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        graph = defaultdict(list)
        for i, p in enumerate(parents[1:], 1):
            graph[p].append(i)
        
        maxScore, cnt = 0, 0
        def dfs(node):
            score, size = 1, n - 1
            for i in graph[node]:
                sz = dfs(i)
                score *= sz
                size -= sz
            if node != 0: 
                score *= size
            nonlocal maxScore, cnt
            if score == maxScore: 
                cnt += 1
            elif score > maxScore:
                maxScore, cnt = score, 1
            return n - size
        
        dfs(0)
        return cnt