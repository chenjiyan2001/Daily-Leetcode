class Solution:
    # 1. O(n) t:48ms(12%) O(1) m:15.9M(67%)
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev