from collections import deque

class Node:
    def __init__(self, data):
        self.head = data
        self.left = None
        self.right = None


def dfs(tree):
    croot = tree
    stack = deque([])
    while True:
        if croot is not None:
            stack.append(croot)
            croot = croot.left
        elif len(stack) > 0:
            croot = stack.pop()
            print(croot.head)
            croot = croot.right
        else:
            break

if __name__ == "__main__":
    tree = Node('a')
    tree.left = Node('b')
    tree.right = Node('c')
    tree.right.left = Node('d')
    tree.right.right = Node('e')
    tree.left.left = Node('f')
    tree.left.right = Node('g')

    dfs(tree)