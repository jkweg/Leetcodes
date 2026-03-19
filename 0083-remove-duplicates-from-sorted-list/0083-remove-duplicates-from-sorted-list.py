# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(None,head)
        s = ListNode(None,head)
        while head is not None:
            if prev.val == head.val:
                prev.next = head.next
                head = head.next
            else:
                prev = head
                head = head.next
        return s.next