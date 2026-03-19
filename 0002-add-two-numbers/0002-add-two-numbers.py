# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s = ListNode(0)
        t = s
        r = 0
        while l1 or l2 or r !=0:
            if l1 is None:
                dig1 = 0
            else:
                dig1 = l1.val
            if l2 is None:
                dig2 = 0
            else:
                dig2 = l2.val
            sum = dig1 + dig2 + r
            dig = sum%10
            r = sum // 10

            new_node = ListNode(dig)
            t.next = new_node
            t = t.next
            if l1 is None:
                None
            else:
                l1 = l1.next
            if l2 is None:
                None
            else:
                l2 = l2.next
        return s.next
        
            

        