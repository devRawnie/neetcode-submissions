class DLL:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = {}
        self.head = DLL(0, 0)
        self.tail = DLL(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev

        self.tail.prev = node
        node.next = self.tail

    def get(self, key: int) -> int:
        if key not in self.hm:
            return -1

        node = self.hm[key]
        self.delete(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            node = self.hm[key]
            self.delete(node)

        self.hm[key] = DLL(key, value)
        self.insert(self.hm[key])

        if len(self.hm) > self.capacity:
            node = self.head.next
            self.delete(node)
            del self.hm[node.key]

