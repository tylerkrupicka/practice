# String Compression
# aabccccaaa -> a2b1c5a3

def compress(s):
    cChar = s[0]
    count = 1
    ret = ""
    for i in range(1, len(s)):
        if s[i] != cChar:
            ret += cChar + str(count)
            cChar = s[i]
            count = 1
        else:
            count += 1
    ret += cChar + str(count)
    return ret
if __name__ == '__main__':
    while True:
        s = input("Enter string: ")
        print(compress(s))
