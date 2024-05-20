#

class ListNode:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None

class HashTable:
  def __init__(self, size=10):
    self.size = size
    self.table = [None] * size

  def _hash(self, key):
    hash_value = 0
    for char in key:
        hash_value += ord(char)
    return hash_value % self.size

  def insert(self, key, value):
    index = self._hash(key)
    if self.table[index] is None:
        self.table[index] = ListNode(key, value)
    else:
        current = self.table[index]
        while True:
            if current.key == key:
                current.value = value  # Update the value if key already exists
                return
            if current.next is None:
                break
            current = current.next
        current.next = ListNode(key, value)

  def get(self, key):
    index = self._hash(key)
    current = self.table[index]
    while current is not None:
        if current.key == key:
            return current.value
        current = current.next
    return None

  def remove(self, key):
    index = self._hash(key)
    current = self.table[index]
    prev = None
    while current is not None:
        if current.key == key:
            if prev is None:
                self.table[index] = current.next
            else:
                prev.next = current.next
            return True
        prev = current
        current = current.next
    return False
