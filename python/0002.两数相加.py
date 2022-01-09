# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 1. O(max(m,n)) t:60ms(36%) m:14.9M(90%)
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> List:
        head = ListNode()
        node = head
        t = 0
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            t = num1 + num2 + t
            node.next = ListNode(t % 10)
            t //= 10
            node = node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if t == 1: # 进位情况t最多只为1
            node.next = ListNode(t)
        return head.next
