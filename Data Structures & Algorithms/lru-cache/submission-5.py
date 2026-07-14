class ListNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.left, self.right = ListNode(0, 0), ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.map = {}
        self.cap = capacity
    
    def remove(self, key):
        cur = self.map.get(key)
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
    
    def insert(self, key):
        prev, next = self.right.prev, self.right
        cur = self.map.get(key)
        prev.next = next.prev = cur
        cur.prev = prev
        cur.next = next

    def get(self, key: int) -> int:
        if key in self.map:
            self.remove(key)
            self.insert(key)
            return self.map.get(key).val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(key)
        self.map[key] = ListNode(key, value)
        self.insert(key)
        
        if len(self.map) > self.cap:
            lru = self.left.next
            self.remove(lru.key)
            del self.map[lru.key]
