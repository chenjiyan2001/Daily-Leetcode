class Solution:
    # # 1. O(1) t:68ms(87%) O(n) m:17.7M(12%) 模拟
    # def __init__(self, head: Optional[ListNode]):
    #     self.nodes = []
    #     while head:
    #         self.nodes.append(head)
    #         head = head.next

    # def getRandom(self) -> int:
    #     return self.nodes[randint(0, len(self.nodes)-1)].val

    # [题解]2. O(n) t:176ms(34%) O(1) m:17.6M(32%) 蓄水池抽样
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        node, idx, res = self.head, 1, self.head.val
        while node:
            if randint(1, idx) == 1:
                res = node.val
            node = node.next
            idx += 1
        return res

