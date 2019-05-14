class Dog:
    dogs = []

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

    def bark(self):
        return "Woof"
    
    @classmethod
    def add(cls, dog):
        cls.dogs.append(dog)

    fido = Dog("Gernam", "Black")
    print(fido.bark())
    Dog.add(fido)