class Solution:
    # [题解]1. O(m+n) t:140ms(79%) m:29.7M(76%) 双指针
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pa, pb = headA, headB
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa