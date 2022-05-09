class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        seq = deque(range(len(s)+1))
        ans = []
        for i in s:
            if i == 'I':
                ans.append(seq.popleft())
            else:
                ans.append(seq.pop())
        return ans + [seq.pop()]