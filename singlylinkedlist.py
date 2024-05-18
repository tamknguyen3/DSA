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




if __name__ == "__main__":
  sll = SinglyLinkedList()

  sll.prepend(1)
  sll.prepend(2)
  sll.prepend(3)
  print("Linked List after prepending:")
  sll.traverse()

  
  sll.append(40)
  sll.append(50)
  print("Linked list after appending:")
  sll.traverse()  

  try:
    print("Element at index 0:", sll.get(0))
    print("Element at index 1:", sll.get(1))
    print("Element at index 2:", sll.get(2))
    print("Element at index 3:", sll.get(3))
    print("Element at index 4:", sll.get(4))  
    print("Element at index 5:", sll.get(5))  # expected to raise IndexError

  except IndexError as e:
    print(e) # Index out of bounds 