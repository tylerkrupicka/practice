# Check Subtree
# Check if a tree is a subtree of another
from bst import BST

def is_subtree(a, b):
    q = []
    q.append(a)
    while len(q):
        n = q.pop(0)
        if n.value == b.value:
            if is_equal(n, b):
                return True
        if n.left != None:
            q.append(n.left)
        if n.right != None:
            q.append(n.right)
    return False

# Check if nodes are equal
# Recursively call on subnodes
def is_equal(a, b):
    if a == None or b == None:
        return True
    if a.value == b.value:
        if is_equal(a.left, b.left) and is_equal(a.right, b.right):
            return True
    return False


if __name__ == '__main__':
    a = BST([1,2,3,4,5,6,7,8,9])
    b = BST([2,3,4])
    print(is_subtree(a.root, b.root))
