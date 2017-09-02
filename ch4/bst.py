# Minimal Tree
# create a binary search tree of minimal height given a sorted array

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self, l):
        self.root = self.build_subtree(l)

    def build_subtree(self, l):
        if len(l) == 0:
            return None
        pivot = len(l) // 2
        n = Node(l[pivot])
        n.left = self.build_subtree(l[:pivot])
        n.right = self.build_subtree(l[pivot + 1:])
        return n
