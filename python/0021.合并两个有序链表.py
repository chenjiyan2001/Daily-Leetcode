class Solution:
    # 1. O(n) t:52ms(5%) O(1) m:14.9M(79%)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        head = ans
        while list1 and list2:
            if list1.val > list2.val:
                ans.next = list2
                list2 = list2.next
            else:
                ans.next = list1
                list1 = list1.next
            ans = ans.next
        if list1:
            ans.next = list1
        else:
            ans.next = list2
        return head.next