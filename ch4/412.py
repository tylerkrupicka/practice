# Paths with sum
# Given a binary tree design an algorithm to find the number of paths that sum to a number.
# list of depths
# create a list of nodes at each depth
from bst import BST

def sum_paths(a, num):
    q = []
    count = 0
    q.append(a)
    while len(q):
        n = q.pop(0)
        count += count_sums(n, 0, num, 0)
        if n.left != None:
            q.append(n.left)
        if n.right != None:
            q.append(n.right)
    return count

# Recursively call on subnodes
def count_sums(n, count, target, value):
    if n == None:
        return count
    print((n.value, count, target, value))
    c1 = count_sums(n.left, count, target, n.value + value)
    c2 = count_sums(n.right, count, target, n.value + value)
    if n.value + value == target:
        count += 1
    return count + c1 + c2
    print("found")

if __name__ == '__main__':
    a = BST([1,2,3,4])
    print(sum_paths(a.root, 3))
