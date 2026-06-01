# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #iterative, 3 ptrs
        curr = head
        pre = None
        post = None

        while curr:
            post = curr.next
            curr.next = pre
            pre = curr
            curr = post

        return pre