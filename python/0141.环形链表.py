class Solution:
    # 1. O(n) t:64ms(26%) O(n) m:19.1M(8%)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d = set()
        if not head: return False
        while head.next:
            if head.next in d: return True
            d.add(head.next)
            head = head.next
        return False
    
    # [题解]2. O(n) t:60ms(43%) O(1) m:18.6M(41%) 快慢指针
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True