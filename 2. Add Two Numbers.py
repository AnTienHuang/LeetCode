# 2. Add Two Numbers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        carry = 0
        while l1 or l2 or carry:
            v1 = 0 if not l1 else l1.val
            v2 = 0 if not l2 else l2.val
            v3 = v1 + v2 + carry
            carry = 0
            if v3 >= 10:
                carry = 1
                v3 = v3 - 10
            cur.next = ListNode(v3)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next