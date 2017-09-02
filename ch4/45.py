# Validate BST
# Check if BT is BST
from bst import BST

def is_bst(t):
    a = recurse(t.root)
    # check if sorted
    for i in range(len(a) - 1):
        if a[i] > a[i+1]:
            return False
    return True

def recurse(t):
    if t == None:
        return []
    a = recurse(t.left)
    a.append(t.value)
    a += recurse(t.right)
    return a

if __name__ == '__main__':
    b = BST([1,2,3,4,5,6,7,8,9])
    print(is_bst(b))
