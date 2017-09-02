# Check balanced
# check if binary tree is balanced
from bst import BST

def height(n):
    if n == None:
        return -1
    return max(height(n.left), height(n.right)) + 1

def is_balanced(n):
    if n == None:
        return True
    diff = height(n.left) - height(n.right)
    if abs(diff) > 1:
        return False
    else:
        return (is_balanced(n.left) and is_balanced(n.right))

if __name__ == '__main__':
    b = BST([1,2,3,4,5,6,7,8,9])
    print(is_balanced(b.root))
