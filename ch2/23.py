# Delete Middle Node
# Delete a node in middle of linked list given only the node to be deleted
from linked_list import *

def remove_middle(n):
    n.data = n.next.data
    n.next = n.next.next

if __name__ == '__main__':
    l = LinkedList()
    l.append("first")
    l.append("first")
    n = l.append("second")
    l.append("third")
    l.append("second")
    print(l)
    remove_middle(n)
    print(l)
