# Stack of Plates
# Implement a data structure containing a flexible number of stacks when a threshold is exceeded

class SetOfStacks:

    def __init__(self, limit):
        self.set = [[]]
        self.limit = limit
        self.index = 0

    def push(self, data):
        if len(self.set[self.index]) >= self.limit:
            # need to expand
            self.set.append([])
            self.index += 1
            print("expanded. new index is " + str(self.index))
        self.set[self.index].append(data)

    def pop(self):
        data = self.set[self.index].pop()
        if len(self.set[self.index]) == 0:
            # emptied a stack
            self.set.pop()
            self.index -= 1
            print("emptied. new index is " + str(self.index))
        return data

if __name__ == '__main__':
    s = SetOfStacks(3)
    while True:
        command = input("Enter command: ")
        if command == "pop":
            print(s.pop())
        elif command == "push":
            data = input("Enter data: ")
            s.push(data)
