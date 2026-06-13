# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head:
            return None

        dummy = ListNode(next=head)
        left, right = dummy, dummy

        for i in range(n):
            right = right.next

        while right and right.next:
            left = left.next
            right = right.next

        temp = left.next
        left.next = temp.next
        temp.next = None

        del temp

        return dummy.next