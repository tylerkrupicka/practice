# string rotation

def is_substring(x, y):
    return x in y

def is_rotation(s1, s2):
    cat = s2 + s2
    return is_substring(s1, cat)

if __name__ == '__main__':
    while True:
        s1 = input("Enter normal string: ")
        s2 = input("Enter possible rotation: ")
        print(is_rotation(s1, s2))
