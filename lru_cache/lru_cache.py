from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.dll = DoublyLinkedList()
        self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key not in self.storage.keys():
            return None
        else:
            value = self.storage[key]
            pair = (key, value)
            curr = self.dll.head
            while not curr.value == pair:
                curr = curr.next
            self.dll.move_to_front(curr)
            return value

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        pair = (key, value)
        if self.size is self.limit and key not in self.storage.keys():
            rem = self.dll.remove_from_tail()[0]
            self.storage.pop(rem)
            self.size -= 1
        if key in self.storage.keys():
            curr = self.dll.head
            while not curr.value[0] == key:
                curr = curr.next
            curr.value = pair
            self.storage[key] = value
            self.dll.move_to_front(curr)
        else:
            self.dll.add_to_head(pair)
            self.storage[key] = value
            self.size += 1
