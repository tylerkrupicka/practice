# Remove Dupes
# Remove duplicates from an unsorted linked list

from linked_list import *

def remove_duplicates(l):
    seen = {}
    n = l.head
    seen[n.data] = True
    while(n.next != None):
        if n.next.data in seen:
            # found a dupe
            if n.next.next == None:
                #end of list
                n.next = None
                return
            else:
                n.next = n.next.next
        seen[n.next.data] = True
        n = n.next

if __name__ == '__main__':
    l = LinkedList()
    l.append("first")
    l.append("first")
    l.append("second")
    l.append("third")
    l.append("second")
    print(l)
    remove_duplicates(l)
    print(l)
