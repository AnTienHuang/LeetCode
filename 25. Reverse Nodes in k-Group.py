# 25. Reverse Nodes in k-Group
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        l = []
        dummy = subhead = ListNode()
        while cur:
            l.append(cur)
            if not len(l) % k:
                tmp = cur.next
                subhead.next = cur
                subhead = l[0]
                for i in range(len(l) - 1, 0, -1):
                    l[i].next = l[i - 1]
                cur = tmp
                l = []
            else:
                cur = cur.next
        if l:
            subhead.next = l[0]
        
        return dummy.next
         
head = ListNode(1)
head.next = ListNode(2)
s = Solution()
s.reverseKGroup(head, 2)