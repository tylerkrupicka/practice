# Common Ancestor
# Find the first common ancestor of two nodes given the root node
from bst import BST

def contains(n, a):
    if n == None:
        return False
    if n.value == a:
        return True
    l = contains(n.left, a)
    r = contains(n.right, a)
    return l or r

def get_ancestor(n, a, b):
    if n == None:
        return False
    l = contains(n.left, a) or contains(n.left, b)
    r = contains(n.right, a) or contains(n.right, b)
    if l and r:
        return n.value
    else:
        l = get_ancestor(n.left, a, b)
        r = get_ancestor(n.right, a, b)
        if l:
            return l
        else:
            return r

if __name__ == '__main__':
    b = BST([1,2,3,4,5,6,7,8,9])
    print(get_ancestor(b.root, 2, 4))
