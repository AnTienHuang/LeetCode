# 146. LRU Cache
# 2nd attempt
class Node:

    def __init__(self, key: int = None, val: int = None, prev: "Node" = None, next: "Node" = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key: node
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None

    def append(self, node: Node):
        node.next = self.left.next
        node.prev = self.left
        self.left.next.prev = node
        self.left.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.append(node)
        return node.val

    def put(self, key: int, val: int):
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, val)
        self.cache[key] = node

        if len(self.cache.keys()) > self.capacity:
            lru = self.right.prev
            self.remove(lru)
            self.cache.pop(lru.key)
            
        self.append(node)

# 1st attempt
# class Node:

#     def __init__(self, key: int = None, val: int = None):
#         self.next = self.prev = None
#         self.key = key
#         self.val = val


# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cap = capacity
#         self.left = self.right = Node()
#         self.left.next = self.right
#         self.right.prev = self.left
#         self.cache = {}

#     def remove(self, node: Node):
#         node.prev.next = node.next
#         node.next.prev = node.prev

#     def append(self, node: Node):
#         node.prev = self.right.prev
#         self.right.prev.next = node
#         node.next = self.right
#         self.right.prev = node

#     def get(self, key: int) -> int:
#         if key in self.cache:
#             n = self.cache[key]
#             self.remove(n)
#             self.append(n)
#             return n.val
#         return -1        

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             node = self.cache[key]
#             node.val = value
#             self.remove(node)
#         else:
#             if len(self.cache) == self.cap:
#                 lru = self.left.next
#                 self.cache.pop(lru.key, None)
#                 self.remove(lru)
#             node = Node(key = key, val = value)
#             self.cache[key] = node
#         self.append(node)