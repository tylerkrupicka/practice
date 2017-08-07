# URLify
# Write a method to replace all spaces in a string with %20. You may assume that the string has sufficient space at the end to hold additional characters, and you are given the true length of the string.

if __name__ == '__main__':
    while True:
        s = input("Enter string with spaces: ")
        print('%20'.join(s.split()))
