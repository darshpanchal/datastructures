class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return self.data

class LinkedList:
    
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
        
    def __repr__(self):
        node = self.head
        nodes=[]
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("End")
        return " >> ".join(nodes)
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def removeNode(self, tnode):
        if not self.head:
            raise Exception("Empty List. Try inserting values.")

        if self.head.data == tnode:
            self.head = self.head.next
            return
        
        prevnode = self.head

        for node in self:
            if node.data == tnode:
                prevnode.next = node.next
                return
            prevnode = node
            
        raise Exception("Error finding %s data." % tnode)
          
    def addFirstnode(self, node):
        node.next = self.head
        self.head = node
        
    def addLastnode(self, node):
        if not self.head:
            self.head = node
            return
        for cnode in self:
            pass
        cnode.next = node

    def addBeforeNode(self, tnode, newnode):
        if not self.head:
            raise Exception("Empty List. Try inserting values.")

        if self.head.data == tnode:
            return self.addFirstnode(newnode)
        
        prev_node = self.head
        
        for node in self:
            if node.data == tnode:
                prev_node.next = newnode
                newnode.next = node
                return
            prev_node = node
            
        raise Exception("Error finding %s data." % tnode)
    
    def addAfterNode(self, tnode, newnode):
        if not self.head:
            raise Exception("Empty List. Try inserting values.")

        for node in self:
            if node.data == tnode:
                newnode.next = node.next
                node.next = newnode
                return

        raise Exception("Error finding %s data." % tnode)
        

if __name__ == "__main__":
    ll = LinkedList(['1','2','3','4'])
    print("Linked List is ", ll)
    ll.removeNode('3')
    print("After removing 3 from LL ", ll)
    ll.addAfterNode('2',Node('3'))
    print(ll)
    ll.addFirstnode(Node('0'))
    print(ll)
    ll.addLastnode(Node('5'))
    print(ll)
