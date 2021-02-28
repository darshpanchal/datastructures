class BST:
    def __init__(self,data):
        self.head = data
        self.left = None
        self.right = None

    def inserttree(self, arr):
        for element in arr:
            if element < self.head:
                if self.left is None:
                    self.left = BST(element)
                else:
                    self.left.inserttree([element])
            else:
                if self.right is None:
                    self.right = BST(element)
                else:
                    self.right.inserttree([element]) 
    
    def gettree(self):
        if self.left:
            self.left.gettree()
        print( self.head, end=" "),
        if self.right:
            self.right.gettree()

    def BSTsearch(self, element):
        if self.head == element:
            return element

        elif self.head < element:
            if self.right is None:
                return "Not Found"
            return self.right.BSTsearch(element)
        
        else:
            if self.left is None:
                return "Not Found"
            return self.left.BSTsearch(element)


if __name__ == "__main__":
    t = BST(7)
    t.inserttree([5,2,8,9,6,20,10,15,100,70,30])
    t.gettree()
    print(t.BSTsearch(1))