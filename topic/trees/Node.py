import os

class Node:
    def __init__(self, d):
        self.left = None
        self.right = None
        self.data = d

def pre_order(n):
    if n == None:
        return

    print(n.data)
    pre_order(n.left)
    pre_order(n.right)

def post_order(n):
    if n == None:
        return

    post_order(n.left)
    post_order(n.right)
    print(n.data)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.right = Node(4)

post_order(root)