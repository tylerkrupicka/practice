# Unique Characters
# Determine if a string is all unique characters. What if you cannot use addititional data structures?

def is_unique_ds(s):
    chars = {}
    for char in s:
        if char in chars:
            return False
        else:
            chars[char] = True
    return True

def is_unique(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    return False
    return True

if __name__ == '__main__':
    while(True):
        s = input("Enter string: ")
        print(is_unique(s))
