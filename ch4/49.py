# BST Sequences
# Given a binary search tree construct possible arrays
# this may or may not work still, i need to revisit it. It could use a verification function.
from bst import BST
import itertools

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

def build_permutations(depths):
    permutations = [depths[0]]
    for key in range(1,len(depths)):
        p = list(itertools.permutations(depths[key]))
        temp = []
        for element in p:
            for perm in permutations:
                temp.append(perm + list(element))
        permutations = temp
    print(permutations)

if __name__ == '__main__':
    b = BST([1,3,5,6,10,11,14])
    depths = create_depths(b)
    build_permutations(depths)
