class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # maps keys : nodes

        self.lru = Node(0, 0)
        self.mru = Node(0, 0)
        
        self.lru.next = self.mru
        self.mru.prev = self.lru
    
    # my helper func oo remove from list
    def remove_node(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    # my helper function to add to list
    def insert_node(self, node):
        prev = self.mru.prev

        prev.next = node
        node.prev = prev

        node.next = self.mru
        self.mru.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove_node(self.cache[key])
            self.insert_node(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])
            self.insert_node(self.cache[key])
            self.cache[key].val = value
        else:
            self.cache[key] = Node(key, value)
            self.insert_node(self.cache[key])
            if len(self.cache) > self.cap:
                lru = self.lru.next
                self.remove_node(self.lru.next)
                del self.cache[lru.key]


