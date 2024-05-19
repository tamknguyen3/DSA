class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # now provides reference to the previous node


class DoublyLinkedList:
  def __init__(self):
      self.head = None
      self.tail = None

  # gets the length of the doubly linked list
  def __len__(self):
      count = 0
      current = self.head
      while current:
          count += 1
          current = current.next
      return count

  # method that adds to the front of the doubly linked list
  def prepend(self, data):
      new_node = DoublyNode(data)
      if not self.head:
          self.head = new_node
          self.tail = new_node
      else:
          new_node.next = self.head
          self.head.prev = new_node
          self.head = new_node

  # method that iterates over a doubly linked list and
  # prints the data stored at every node
  def traverse(self):
      current = self.head
      while current:
          print(current.data, end=" <-> ")
          current = current.next
      print("None")

  # method to traverse the doubly linked list backwards
  def traverse_backward(self):
      current = self.tail
      while current:
          print(current.data, end=" <-> ")
          current = current.prev
      print("None" if self.tail is None else "")

  # method to get the value stored in kth element
  def get(self, k):
      try:
          if k < 0 or k >= len(self):
              raise IndexError("Index out of bounds")
          current = self.head
          count = 0
          while current:
              if count == k:
                  return current.data
              current = current.next
              count += 1
      except IndexError as e:
          print(e)

  # method that creates a node and adds it to the back of the list
  def append(self, data):
      new_node = DoublyNode(data)
      if self.head is None:
          self.head = new_node
          self.tail = new_node
      else:
          self.tail.next = new_node
          new_node.prev = self.tail
          self.tail = new_node

  def insert(self, data, index):
      try:
          if index < 0 or index > len(self):
              raise IndexError("Index out of bounds")
          elif index == 0:
              self.prepend(data)
          else:
              new_node = DoublyNode(data)
              current = self.head
              for _ in range(index):
                  if current is None:
                      raise IndexError("Index out of bounds")
                  current = current.next
              if current is None:
                  # If current is None, it means the index is equal to the length of the list
                  self.append(data)
              else:
                  new_node.next = current
                  new_node.prev = current.prev
                  if current.prev:
                      current.prev.next = new_node
                  else:
                      self.head = new_node
                  current.prev = new_node
      except IndexError as e:
          print(e)

  def delete(self, index):
      if index == 0:
          if self.head is None:
              raise IndexError("Index out of bounds")
          if self.head == self.tail:
              self.head = None
              self.tail = None
          else:
              self.head = self.head.next
              self.head.prev = None
      else:
          current = self.head
          for _ in range(index):
              if current is None:
                  raise IndexError("Index out of bounds")
              current = current.next
          if current == self.tail:
              current.prev.next = None
              self.tail = current.prev
          else:
              current.prev.next = current.next
              current.next.prev = current.prev

if __name__ == "__main__":
  # Create an instance of DoublyLinkedList
  dll = DoublyLinkedList()

  # Test prepend method
  dll.prepend(10)
  dll.prepend(20)
  dll.prepend(30)
  print("After prepend:")
  dll.traverse()  # Expected output: 30 <-> 20 <-> 10 <-> None

  # Test append method
  dll.append(40)
  dll.append(50)
  print("After append:")
  dll.traverse()  # Expected output: 30 <-> 20 <-> 10 <-> 40 <-> 50 <-> None

  # Test insert method
  dll.insert(25, 2)
  dll.insert(5, 0)
  dll.insert(60, 6)
  print("After insert:")
  dll.traverse()  # Expected output: 5 <-> 30 <-> 20 <-> 25 <-> 10 <-> 40 <-> 60 <-> 50 <-> None

  # Test delete method
  dll.delete(2)
  dll.delete(0)
  dll.delete(len(dll) - 1)
  print("After delete:")
  dll.traverse()  # Expected output: 30 <-> 20 <-> 10 <-> 40 <-> None

  # Test traverse_backward method
  print("Backward traversal:")
  dll.traverse_backward()  # Expected output: 40 <-> 10 <-> 20 <-> 30 <-> None

  # Test get method
  print("Element at index 0:", dll.get(0))  # Expected output: 30
  print("Element at index 1:", dll.get(1))  # Expected output: 20
  print("Element at index 2:", dll.get(2))  # Expected output: 10

