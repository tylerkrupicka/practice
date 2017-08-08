# Sum Lists
# you have two numbers represented as a linked list. numbers are stored in reverse order.
# add the two numbers and return a linked list

from linked_list import *

def add(l1,l2):
    val = str(convert(l1) + convert(l2))
    val = val[::-1]
    l = LinkedList()
    for char in val:
        l.append(int(char))
    return l

def convert(l):
    s = ""
    n = l.head
    while(n != None):
        s = str(n.data) + s
        n = n.next
    return int(s)

if __name__ == '__main__':
    l1 = LinkedList()
    l1.append(7)
    l1.append(1)
    l1.append(6)
    l2 = LinkedList()
    l2.append(5)
    l2.append(9)
    l2.append(2)
    print(l1)
    print(l2)
    l = add(l1,l2)
    print(l)
