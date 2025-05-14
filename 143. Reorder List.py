# 143. Reorder List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # now slow.next will be the right half that will be reversely inserted

        # reverse the right half
        prev, cur = None, slow.next
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        # reorder the nodes
        dummy = ListNode(0, head)
        left, right = head, prev
        slow.next = None # separate left and right halfs
        while left:
            tmp1 = left.next
            tmp2 = right.next if right else None
            dummy.next = left
            dummy.next.next = right if right else None
            dummy = dummy.next.next
            left = tmp1
            right = tmp2
