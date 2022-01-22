class Solution:
    # 1. O(n) 328ms O(n) 29.2M(59%)
    def minJumps(self, arr: List[int]) -> int:
        hash = defaultdict(list)
        for i, num in enumerate(arr):
            hash[num].append(i)
        walked = set()
        queue = deque([0])
        walked.add(0)
        step = 0
        while queue:
            size = len(queue)
            for iter in range(size):
                node = queue.popleft()
                walked.add(node)
                if node == len(arr)-1: return step
                for n in hash[arr[node]]:
                    if n not in walked:
                        queue.append(n)
                        walked.add(n)
                del hash[arr[node]]
                if 0 <= node - 1 and node - 1 not in walked:
                    queue.append(node - 1)
                    walked.add(node - 1)
                if node + 1 < len(arr) and node + 1 not in walked:
                    queue.append(node + 1)
                    walked.add(node + 1)
            step += 1