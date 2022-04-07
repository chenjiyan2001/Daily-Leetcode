class Solution:
    # [题解]1. O(n) t:116ms(94%) O(n) m:21.8M(76%) 拓扑排序+BFS
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree = [0] * n
        graph = defaultdict(list)
        for i1, i2 in edges:
            in_degree[i1] += 1
            in_degree[i2] += 1
            graph[i1].append(i2)
            graph[i2].append(i1)
        nodes = [i for i, v in enumerate(in_degree) if v <= 1]
        while n > 2:
            n -= len(nodes)
            nxt = []
            for node in nodes:
                for other in graph[node]:
                    in_degree[other] -= 1
                    if in_degree[other] == 1:
                        nxt.append(other)
            nodes = nxt
        return nodes