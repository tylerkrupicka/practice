# Intersection
# find the node where two linked lists intersect

from linked_list import *

def intersect(l1, l2):
    # determine if they intersect
    n1 = l1.head
    while(n1.next != None):
        n1 = n1.next
    n2 = l2.head
    while(n2.next != None):
        n2 = n2.next
    if n1 != n2:
        return False # not an Intersection
    # find Intersection
    length1 = len(l1)
    length2 = len(l2)
    if length2 > length1:
        l1, l2 = l2, l1
    # l1 is longest
    dif = length1 - length2
    n1 = l1.head
    for i in range(dif): #make same length
        n1 = n1.next
    n2 = l2.head
    while(n1.next != None):
        if n1 == n2:
            return n1
        n1 = n1.next
        n2 = n2.next

if __name__ == '__main__':
    l1 = LinkedList()
    l1.append("first")
    l1.append("second")
    t = l1.append("third")
    l1.append("fourth")
    l2 = LinkedList()
    f = l2.append("first2")
    f.next = t
    print(l1)
    print(l2)
    print(intersect(l1,l2))
