# Palindrome
# Check whether a linked list is a Palindrome
from linked_list import *

def is_palindrome(l):
    return recurse(l.head, "")
def recurse(n, s):
    if n == None:
        return s == s[::-1]
    s += n.data
    return recurse(n.next, s)

if __name__ == '__main__':
    l = LinkedList()
    l.append("k")
    l.append("a")
    l.append("y")
    l.append("a")
    l.append("k")
    print(is_palindrome(l))
