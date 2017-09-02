# list of depths
# create a list of nodes at each depth
from bst import BST

def create_depths(t):
    lists = {}
    recurse(lists, t.root, 0)
    return lists

def recurse(lists, node, depth):
    if node == None:
        return
    if depth not in lists:
        lists[depth] = []
    lists[depth].append(node.value)
    recurse(lists, node.left, depth + 1)
    recurse(lists, node.right, depth + 1)

if __name__ == '__main__':
    b = BST([1,2,3,4,5,6,7,8,9])
    print(create_depths(b))
