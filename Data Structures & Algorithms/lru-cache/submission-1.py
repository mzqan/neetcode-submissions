class LRUCache:
    class Node:
        def __init__(self, key = None, val = None):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None
        
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    def _addToFront(self, node):
        prev = self.head
        next = self.head.next

        node.next = next
        next.prev = node

        prev.next = node
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._addToFront(node)

            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._addToFront(node)
        else:
            if len(self.cache) >= self.capacity:
                last = self.tail.prev
                del self.cache[last.key]
                self._remove(last)

            node = self.Node(key, value) 
            self._addToFront(node)
            self.cache[key] = node
        

