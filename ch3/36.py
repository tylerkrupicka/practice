#Animal Shelter
# Animal shelter is a queue. People must adopt the oldest animal or can select dog or cat.
# enqueue, dequeueAny, dequeueDog, dequeueCat

class AnimalShelter:

    def __init__(self):
        self.time = 0
        self.dogQ = []
        self.catQ = []

    def enqueue(self, animal):
        if animal == "cat":
            self.catQ.append(self.time)
        else:
            self.dogQ.append(self.time)
        self.time += 1

    def dequeueDog(self):
        return self.dogQ.pop(0)

    def dequeueCat(self):
        return self.catQ.pop(0)

    def dequeueAny(self):
        dog = self.dogQ[0]
        cat = self.catQ[0]
        if cat < dog:
            return ("cat", self.catQ.pop(0))
        return ("dog", self.dogQ.pop(0))

if __name__ == '__main__':
    a = AnimalShelter()
    while True:
        c = input("> ")
        if c == "enqueue":
            animal = input("animal> ")
            a.enqueue(animal)
        elif c == "dequeueDog":
            print(a.dequeueDog())
        elif c == "dequeueCat":
            print(a.dequeueCat())
        elif c == "dequeue":
            print(a.dequeueAny())
