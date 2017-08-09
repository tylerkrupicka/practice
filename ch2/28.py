# Loop Detection
# return the node at loop beginning of circular linked list

from linked_list import *

def detect_loop(l):
    r1 = l.head
    r2 = l.head
    first = True
    while(first or r1 != r2):
        first = False
        r1 = r1.next
        r2 = r2.next.next
        if r1 == None or r2 == None:
            return "Not a loop"
    #find Intersection
    r2 = l.head
    while(r1 != r2):
        r1 = r1.next
        r2 = r2.next
    return r1

if __name__ == '__main__':
    l1 = LinkedList()
    first = l1.append("first")
    l1.append("second")
    l1.append("third")
    l1.append("fourth")
    fifth = l1.append("fifth")
    fifth.next = first
    print(detect_loop(l1))
