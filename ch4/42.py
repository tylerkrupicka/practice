# Minimal Tree
# create a binary search tree of minimal height given a sorted array

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def construct_tree(l):
    return build_subtree(l)

def build_subtree(l):
    if len(l) == 0:
        return None
    pivot = len(l) // 2
    n = Node(l[pivot])
    n.left = build_subtree(l[:pivot])
    n.right = build_subtree(l[pivot + 1:])
    return n

def print_tree(root):
    if root.left:
        print_tree(root.left)
    print(root.value)
    if root.right:
        print_tree(root.right)
        
if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    t = construct_tree(l)
    print_tree(t)
