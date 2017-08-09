# sort stack
# make a stack which always has the smallest items on top. may only use one additional temporary stack.
# stack supports push, pop, peek, isEmpty

class SortedStack:

    def __init__(self):
        self.stack = []
        self.temp = []

    def push(self, data):
        if len(self.stack) == 0:
            self.stack.append(data)
        else:
            # need to insert in minimum
            while(len(self.stack) > 0 and self.stack[-1] < data):
                self.temp.append(self.stack.pop())
            self.stack.append(data)
            while(len(self.temp) > 0):
                self.stack.append(self.temp.pop())

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

if __name__ == '__main__':
    s = SortedStack()
    while True:
        c = input("command> ")
        if c == "push":
            d = input("data> ")
            s.push(d)
        elif c == "pop":
            print(s.pop())
        elif c == "peek":
            print(s.peek())
        elif c == "isempty":
            print(s.isEmpty())
