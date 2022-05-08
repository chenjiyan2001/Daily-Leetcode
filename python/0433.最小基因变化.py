class Solution:
    # 1. O(n) t:36ms(68%) O(n) m:15.2M(5%) BFS
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        q = deque([(start, 0)])
        vis = set()
        n = len(end)
        while q:
            nxt, times = q.popleft()
            if nxt == end:
                return times
            for seq in bank:
                if seq in vis:
                    continue
                cur = 0
                for i in range(n):
                    if nxt[i] != seq[i]:
                        cur += 1
                if cur == 1:
                    q.append((seq, times+1))
                    vis.add(seq)
        return -1