import doublyLinkedList
class Stack:
  def __init__(self):
    self.stack=doublyLinkedList.LinkedList()

  def isEmpty(self):
    if(self.stack.size==0):
      return True
    else:
      return False

  def display(self):
    self.stack.printList()

  def push(self,data):
    self.stack.addTail(data)
  
  def pop(self):
    self.stack.delTail
  
  def top(self):
    c = self.stack.head
    while c.next!=None:
      c = c.next
    return c.data

  def bubbleSort(self):
    self.stack.bubbleSort()