class Solution:
    # 1. O(n) t:64ms(58%) O(1) m:18.2M(48%)
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        p = dummy
        while p:
            if p.next and p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next