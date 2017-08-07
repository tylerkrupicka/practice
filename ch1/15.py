# One Away
# Determine whether a string is one insert, remove, or replace away from another

def one_away(in1, in2):
    count = 0
    if(len(in1) == len(in2)):
        # its a replace
        for i in range(len(in1)):
            if in1[i] != in2[i]:
                count += 1
        # check differences found
        if count > 1:
            return False
    else:
        s1, s2 = in1, in2
        if (len(in1) < len(in2)):
            s2, s1 = in1, in2 # first will always be longer
        if len(s1) - len(s2) > 1:
            return False
        for i in range(len(s1)-1):
            if s1[i] != s2[i]: # we found an extra letter in s1
                new = s1[:i] + s1[i+1:]
                return new == s2

    return True

if __name__ == '__main__':
    while True:
        in1 = input("Enter first word: ")
        in2 = input("Enter second word: ")
        print(one_away(in1, in2))
