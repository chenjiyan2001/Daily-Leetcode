# 1. O(logn) t:560ms(85%) O(n) m:59.7M(5%)
class StockPrice:

    def __init__(self):
        self.price = defaultdict(int)
        self.cur = -1
        self.min = []
        self.max = []

    def update(self, timestamp: int, price: int) -> None:
        if timestamp > self.cur: self.cur = timestamp
        self.price[timestamp] = price
        heapq.heappush(self.min, [price, timestamp])
        heapq.heappush(self.max, [-price, timestamp])

    def current(self) -> int:
        return self.price[self.cur]

    def maximum(self) -> int:
        while True:
            price, stamp = self.max[0]
            if -price == self.price[stamp]: return -price
            heapq.heappop(self.max)

    def minimum(self) -> int:
        while True:
            price, stamp = self.min[0]
            if price == self.price[stamp]: return price
            heapq.heappop(self.min)

from sortedcontainers import SortedList

# # [题解]2. O(logn) t:688ms(62%) O(n) m:52.3M(39%)
# class StockPrice:
#     def __init__(self):
#         self.price = SortedList()
#         self.timePriceMap = {}
#         self.maxTimestamp = 0

#     def update(self, timestamp: int, price: int) -> None:
#         if timestamp in self.timePriceMap:
#             self.price.discard(self.timePriceMap[timestamp])
#         self.price.add(price)
#         self.timePriceMap[timestamp] = price
#         self.maxTimestamp = max(self.maxTimestamp, timestamp)

#     def current(self) -> int:
#         return self.timePriceMap[self.maxTimestamp]

#     def maximum(self) -> int:
#         return self.price[-1]

#     def minimum(self) -> int:
#         return self.price[0]