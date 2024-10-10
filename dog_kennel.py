class Dog:
    def __init__(self, dog_name):
        self._dog_name = dog_name

    @property
    def name(self):
        return self._dog_name

    def bark(self):
        print("woof! woof!")

class Cat:
    def __init__(self, cat_name):
        self._cat_name = cat_name

    @property
    def name(self):
        return self._cat_name

    def meow(self):
        print("meow! meow!")

class DogKennel:
    DOGS: list[Dog] = []

    def add_dog(self, dog: Dog):
        self.DOGS.append(dog)

    @classmethod
    def show_dogs(cls):
        for dog in cls.DOGS:
            print(dog.name)

kennel = DogKennel()

d1: Dog = Dog("Nellie")
kennel.add_dog(d1)
d2: Dog = Dog("Andy")
kennel.add_dog(d2)
c1: Cat = Cat("Aye-aye")
# kennel.add_dog(c1)

kennel.show_dogs()
