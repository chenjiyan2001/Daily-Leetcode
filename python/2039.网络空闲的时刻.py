class Solution:
    # [题解]1. O(n+m) t:544ms(75%) O(n+m) m:54.7M(82%) BFS
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        graph = defaultdict(list)
        dist = [inf] * n
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        stack = deque([(0,0)])
        dist[0] = 0
        while stack:
            node, d = stack.popleft()
            dist[node] = d
            for next in graph[node]:
                if dist[next] == inf:
                    dist[next] = d + 1
                    stack.append((next, d + 1))
        ans = 0
        for i in range(n):
            d, p = dist[i] * 2, patience[i]
            ans = max(ans, (d - 1) // p * p + d if p else 0)
        return ans + 1