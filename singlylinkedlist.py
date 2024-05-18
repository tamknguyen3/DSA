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
    new_node = Node(data) # create new node 
    new_node.next = self.head # new node points to current head
    self.head = new_node # update head

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

if __name__ == "__main__":
  sll = SinglyLinkedList()

  sll.prepend(1)
  sll.prepend(2)
  sll.prepend(3)

  print("Linked List after prepending:")
  sll.traverse()

  try:
    print("Element at index 0:", sll.get(0))
    print("Element at index 1:", sll.get(1))
    print("Element at index 2:", sll.get(2))
    print("Element at index 3:", sll.get(3))


  except IndexError as e:
    print(e) # Index out of bounds 