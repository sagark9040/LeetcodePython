import os

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

root = Node(1)

def pre_order(Node n):
    if n == None:
        break

    print(n.data)
    pre_order(n.left)
    pre_order(n.right)

