# each node contains data and a reference to the next node in the sequence
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head = None 

  # method that adds to the front of the list
  def prepend(self, data):
    new_node = Node(data)               # create new node 
    new_node.next = self.head           # new node points to current head
    self.head = new_node                # update head

  # method that iterates over a linked list and
  # prints the data stored at every node
  def traverse(self):
    current = self.head
    while current:
      print(current.data, end=" -> ")
      current = current.next
    print("None")

  # method to get the value stored in kth element 
  def get(self, k):
    current = self.head
    count = 0
    while current:
      if count == k:
        return current.data
      
      # update pointer/counter
      current = current.next
      count += 1
    raise IndexError("Index out of bounds")
  
  # method that creates a node and adds it to the back of the list
  def append(self, data):
    new_node = Node(data)         # create new node
    if self.head is None:         # edge case, there's no current node in list to append to 
      self.head = new_node
      return
    
    last = self.head              # traverse tail pointer to reference its next to the new node 
    while last.next:
      last = last.next 
    last.next = new_node

  # method that adds a new node at the given index
  def insert(self, data, index):
    new_node = Node(data)      
    if index == 0:                 # edge case, inserting at the head/front
      new_node.next = self.head
      self.head = new_node
      return
    
    target = self.head
    target_index = 0            
    while target is not None and target_index < index - 1:
      target = target.next
      target_index += 1

    if target is None:
      raise IndexError("Index out of bounds")
    
    new_node.next = target.next   # reassigning the pointers
    target.next = new_node

  # method that removes a node at the given index
  def delete(self, index):
    if self.head is None:         # list is emptythere's nothing to remove 
      raise IndexError("Index out of bounds")
    
    current = self.head
    if index == 0:                        # removing the head 
      self.head = current.next
      return
    
    prev = None 
    current_index = 0
    while current is not None and current_index < index:
      prev = current
      current = current.next 
      current_index += 1

    if current is None:             # reaches the end before the given index
      raise IndexError("Index out of bounds")
    
    prev.next = current.next 
    current = None

  # iteration methods 
  def __iter__(self):
    self._iterator = self.head
    return self
  
  def __next__(self):
    if self._iterator is None:
      raise StopIteration
    current_data = self._iterator.data
    self._iterator = self._iterator.next
    return current_data



if __name__ == "__main__":
  sll = SinglyLinkedList()

  sll.prepend(10)
  sll.prepend(20)
  sll.prepend(30)
  print("Linked List after prepending:")
  sll.traverse()

  
  sll.append(40)
  sll.append(50)
  print("Linked list after appending:")
  sll.traverse()  


  sll.insert(25, 2)
  sll.insert(5, 0)
  sll.insert(60, 6)

  print("Linked list after various insertions:")
  sll.traverse()  # Expected output: 5 -> 30 -> 20 -> 25 -> 10 -> 40 -> 60 -> 50 -> None

  
  try:
    print("Element at index 0:", sll.get(0))
    print("Element at index 1:", sll.get(1))
    print("Element at index 2:", sll.get(2))
    print("Element at index 3:", sll.get(3))
    print("Element at index 4:", sll.get(4))  
    print("Element at index 5:", sll.get(5))  # expected to raise IndexError

  except IndexError as e:
    print(e) # Index out of bounds 

  print("Iterating over the list:")
  for data in sll:
    print(data, end=" -> ")
  print("None")