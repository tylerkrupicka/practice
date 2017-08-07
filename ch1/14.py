# Palindrome Permutations
# Determine if a permutation of a given string is a palindrome.

def is_palindrome(s):
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    print(counts)
    center = True
    if len(s) % 2 != 0:
        center = False
    for key, value in counts.items():
        if value % 2 != 0:
            if center == True:
                return False
            else:
                center == True

    return True

if __name__ == '__main__':
    while True:
        s = input("String: ")
        s = s.replace(" ", "")
        print(is_palindrome(s))
