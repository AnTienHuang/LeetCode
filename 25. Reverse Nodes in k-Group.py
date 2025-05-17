# 25. Reverse Nodes in k-Group
# Definition for singly-linked list.
# from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        i = 0
        dummy = tail = ListNode(0, head)
        subhead = head
        while cur:
            i += 1
            if i == k: 
                prev = tmp = cur.next
                while subhead != tmp:
                    tmp1 = subhead.next
                    subhead.next = prev
                    prev = subhead
                    subhead = tmp1
                next_tail = tail.next
                tail.next = prev
                tail = next_tail
                cur = subhead
                i = 0
            else:
                cur = cur.next
        
        return dummy.next
         
# head = ListNode(0)
# cur = head
# for i in range(1, 6): 
#     node = ListNode(i)
#     cur.next = node
#     cur = cur.next
# s = Solution()
# s.reverseKGroup(head.next, 2)