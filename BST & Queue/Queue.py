from BinarySearchTree import BinarySearchTree

class Queue:
    def __init__(self):
        self.queue=BinarySearchTree()
        self.size = 0
  
    def isEmpty(self):
        if (self.size==0):
            return True
        else:
            return False
    
    def display(self):
        self.queue.revInorder(self.queue.root)

    def enqueue(self,data):
        self.queue.insert(data)
        self.size += 1
  
    def dequeue(self):
        self.queue.remove_max(self.queue.root)
        self.size -= 1

    def front(self):
        return self.queue.max
    
    def back(self):
        return self.queue.tail.data