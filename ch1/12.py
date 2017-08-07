# Check Permutation
# Given two strings, write a method to decide if one is a permutation of the other.

def is_permutation(s1,s2):
    if len(s1) != len(s2):
        return False
    if sorted(s1) == sorted(s2):
        return True
    return False

if __name__ == '__main__':
    while(True):
        s1 = input("String i1: ")
        s2 = input("String 2: ")
        print(is_permutation(s1, s2))
