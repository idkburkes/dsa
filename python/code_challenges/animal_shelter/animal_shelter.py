
class Dog(object):
    def __init__(self, name = 'Dog'):
        self.name = name
            
class Cat(object):
    def __init__(self, name = 'Cat'):
        self.name = name


class AnimalShelter:

    def __init__(self):
        self.dogs = []
        self.cats = []

    def enqueue(self, animal):
        if type(animal) is Dog:
            self.dogs.append(animal)
        elif type(animal) is Cat:
            self.cats.append(animal)

    def dequeue(self, pref):
        if pref.lower() == 'dog':
            if len(self.dogs):
                return self.dogs.pop(0)
            else:
                return None    
        elif pref.lower() == 'cat':
            if len(self.cats):
                return self.cats.pop(0)
            else:
                return None
        else:
            return None
