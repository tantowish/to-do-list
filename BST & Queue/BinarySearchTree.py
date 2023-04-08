class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root=None
        self.size=0
    def insert(self,data):
        newNode=Node(data)
        if self.root==None:
            self.root=newNode
        else:
            c = self.root
            while True:
                if data[1]<c.data[1]: # Cek kiri
                    if c.left == None:
                        c.left = newNode
                        self.size+=1
                        return
                    else:
                        c = c.left
                else: # Cek kanan
                    if c.right == None:
                        c.right = newNode
                        self.size+=1
                        return
                    else:
                        c = c.right
        self.size+=1
                
    def inorder(self,c):
        if c==None:
            return
        self.inorder(c.left)
        print(c.data)
        self.inorder(c.right)

    def revInorder(self,c):
        if c==None:
            return
        self.revInorder(c.right)
        print(c.data, end=" ")
        self.revInorder(c.left)

    def max(self):
        if self.root is None:
            return None
        
        while self.root.right is not None:
            self.root = self.root.right
            
        return self.root.data

    def min(self):
        if self.root is None:
            return None
        
        # traverse the tree to the leftmost node
        while self.root.left is not None:
            self.root = self.root.left
        
        # root now contains the minimum value
        return self.root.data

    def remove_max(self, node):
        if node is None:
            return None
        parent = None
        current = node
        while current.right is not None:
            parent = current
            current = current.right
        if parent is None:
            # Max adalah root
            self.root = current.left
        else:
            parent.right = current.left
        self.size-=1
        print(current.data[0], "selesai")