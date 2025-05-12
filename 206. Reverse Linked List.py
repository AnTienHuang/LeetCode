# 206. Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return []
        
        prev, cur = None, ListNode()
        while head:
            prev = cur.next
            cur.next = head
            head = head.next
            cur.next.next = prev

        return cur.next
