# Partition
# Partition a linked linked less such that all values less than x come before values >= x

from linked_list import *

def partition(l, pivot):
    before = LinkedList()
    cur_b = None
    after = LinkedList()
    n = l.head
    while(n != None):
        if n.data < pivot:
            # goes in before
            cur_b = before.append(n.data)
        else:
            after.append(n.data)
        n = n.next
    cur_b.next = after.head
    return before

if __name__ == '__main__':
    l = LinkedList()
    l.append(3)
    l.append(5)
    l.append(8)
    l.append(5)
    l.append(10)
    l.append(2)
    l.append(1)
    print(l)
    l = partition(l, 5)
    print(l)
