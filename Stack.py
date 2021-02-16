# Stack implementation using linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, nodes=None):
        self.head = Node('None')
        self.depth = 0
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        output = []
        cursor = self.head.next
        while cursor:
            output.append(str(cursor.data))
            cursor = cursor.next
        return " >> ".join(output)
    
    def stackempty(self):
        return self.depth == 0

    def push(self, data):
        node = Node(data)
        node.next = self.head.next
        self.head.next = node
        self.depth += 1

    def pop(self):
        if self.stackempty():
            raise Exception("Stack is empty. Try pushing values.")
        value = self.head.next
        self.head.next = self.head.next.next
        self.depth -= 1
        return value
    
    def getDepth(self):
        return self.depth

if __name__ == "__main__":
    s = Stack()
    print("Is stack empty? ", s.stackempty())
    print("Pushing some values in stack..")
    for i in "abcdefg":
        s.push(i)
    print("Stack is : ", s)
    for i in range(3):
        s.pop()
    print("Stack after pop : ", s)
    print("Size of Stack : ", s.getDepth())