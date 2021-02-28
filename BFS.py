from collections import deque


class Node:
    def __init__(self, data):
        self.head = data
        self.left = None
        self.right = None


def bfs(tree):
    queue = deque([tree])
    while len(queue) > 0:
        node = queue.popleft()
        print(node.head)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


if __name__ == "__main__":
    tree = Node('a')
    tree.left = Node('b')
    tree.right = Node('c')
    tree.right.left = Node('d')
    tree.right.right = Node('e')
    tree.left.left = Node('f')
    tree.left.right = Node('g')

    bfs(tree)
