# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l1, l2 = head, slow.next
        slow.next = None

        #reverse l2
        pre = None
        curr = l2
        post = None

        while curr:
            post = curr.next
            curr.next = pre
            pre = curr
            curr = post

        l2 = pre

        while l1 and l2:
            temp1, temp2 = l1.next, l2.next
            l2.next = l1.next
            l1.next = l2
            l1, l2 = temp1, temp2