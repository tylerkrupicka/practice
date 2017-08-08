# kth to last
# return the kth to last node in a linked list
# this solution is 2n by finding length
# n solution is have two pointers, one k steps behind the other
from linked_list import *

def k_to_last(l, k):
    index = len(l) - k
    n = l.head
    i = 0
    while(i != index):
        n = n.next
        i += 1
    return n


if __name__ == '__main__':
    l = LinkedList()
    l.append("first")
    l.append("first")
    l.append("second")
    l.append("third")
    l.append("second")
    print(l)
    n = k_to_last(l, 3)
    print(n)
