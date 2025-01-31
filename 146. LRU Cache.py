class Node:

    def __init__(self, key: int = None, val: int = None):
        self.next = self.prev = None
        self.key = key
        self.val = val


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.left = self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {}

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def append(self, node: Node):
        node.prev = self.right.prev
        self.right.prev.next = node
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            n = self.cache[key]
            self.remove(n)
            self.append(n)
            return n.val
        return -1        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
        else:
            if len(self.cache) == self.cap:
                lru = self.left.next
                self.cache.pop(lru.key, None)
                self.remove(lru)
            node = Node(key = key, val = value)
            self.cache[key] = node
        self.append(node)