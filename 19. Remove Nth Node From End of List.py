# 19. Remove Nth Node From End of List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []

        cur = head
        while cur:
            nodes.append(cur)
            if len(nodes) == n + 2:
                nodes.pop(0)
            cur = cur.next
        
        if len(nodes) == n:
            return head.next
        else:
            nodes[0].next = None if len(nodes) < 3 else nodes[2]
            return head
