# Queue via stacks
# Implement a queue implemented using two stacks

class Queue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def add(self, data):
        self.s1.append(data)

    def remove(self):
        # read all from s1 in to s2
        while(len(self.s1) > 0):
            self.s2.append(self.s1.pop())
        # get the top
        d = self.s2.pop()
        # put data back in s1
        while(len(self.s2) > 0):
            self.s1.append(self.s2.pop())
        return d

if __name__ == '__main__':
    q = Queue()
    while True:
        command = input("> ")
        if command == "add":
            d = input("data> ")
            q.add(d)
        elif command == "remove":
            print(q.remove())
        else:
            print("command not found")
