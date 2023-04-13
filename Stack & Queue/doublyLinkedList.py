# Class Node untuk membuat Node dari setiap data yang dimasukkan
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

# Double Linked List
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addHead(self,data): 
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else :
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.size += 1

    def addTail(self,data):
        newNode = Node(data)
        if self.tail == None:
            self.head = newNode
            self.tail = newNode
        else :
            newNode.prev=self.tail
            self.tail.next=newNode
            self.tail = newNode
        self.size += 1
    
    def addMid(self,index,data):
        if index < 0 or index >self.size:
            return
        newNode = Node(data)
        if self.head == None or self.tail == None:
            self.head = newNode
            self.tail = newNode
        c = self.head
        if index == 0:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        elif index == self.size:
            newNode.prev=self.tail
            self.tail.next=newNode
            self.tail = newNode
        else :
            for i in range(index-1) :
               c = c.next
            newNode.next = c.next
            c.next = newNode
            newNode.prev = c
            newNode.next.prev = newNode
        self.size += 1

    def delHead(self):
        if self.head==None:
            return
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1
    
    def delTail(self):
        if self.tail==None:
            return
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1

    def delMid(self,index):
        if index < 0 or index >=self.size:
            return
        if self.head == None or self.tail == None:
            return
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index == self.size-1:
            self.tail = self.tail.prev
            self.tail.next = None
        else :
            c=self.head
            for i in range(index-1):
                c=c.next
            c.next = c.next.next
            c.next.prev = c
        self.size -= 1
    
    def toList(self):
        node = [[],[]]
        h = self.head
        t = self.tail
        for i in range(2):
            for j in range(self.size):
                if i == 0:
                    node[i].append(h.data)
                    h=h.next
                else:
                    node[i].append(t.data)
                    t=t.prev
        return node
    
    def printList(self):
        c = self.head
        while c!=None:
            print(c.data)
            c=c.next

    def printReverse(self):
        c = self.tail
        while c!=None:
            print(c.data)
            c=c.prev

    def swapNode(self, A, B):
        if A.data[1] == B.data[1]:
            return
        if(A==self.head):
          A.next = B.next
          B.next.prev=A
          B.next = A
          A.prev = B
          self.head = B
          self.head.prev = None

        elif(B==self.tail):
          A.prev.next = B
          B.prev = A.prev
          B.next = A
          A.prev =B
          self.tail =A
          self.tail.next = None
        else:
          A.next = B.next
          B.next.prev=A
          B.next = A
          B.prev = A.prev
          A.prev.next = B
          A.prev = B


    def bubbleSort(self):
    # print(stack.head.data[1])
        for i in range(self.size-1):
          for j in range(self.size-1):
            # print(i,j)
            current = self.head
            for k in range(j):
              current=current.next
            # print("current=",current.data)
            # print(self.stack.toList())
            # print("dasda\n",self.printList())
            if (current.data[1]<current.next.data[1]):
              self.swapNode(current,current.next)

