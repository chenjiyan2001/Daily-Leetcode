class RecentCounter:
    # 1. O(1) t:212ms(89%) O(L) m:19.9M(14%) 队列 
    def __init__(self):
        self.request = deque([])

    def ping(self, t: int) -> int:
        self.request.append(t)
        while self.request[0] < t - 3000:
            self.request.popleft()
        return len(self.request)