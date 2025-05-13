# 138. Copy List with Random Pointer
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {None: None} # old node: new node
        prev = None
        cur = head
        while cur:
            new_node = Node(cur.val, None, cur.random)
            old_to_new[cur] = new_node
            if prev:
                prev.next = new_node
            prev = old_to_new[cur]
            cur = cur.next
        
        cur = old_to_new[head]
        while cur:
            cur.random = old_to_new[cur.random]
            cur = cur.next
        
        return old_to_new[head]
