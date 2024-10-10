colors = list()
colors = []   # shortcut for list()
things = {}   # shortcut for dict()
stuff = ()  # shortcut for tuple()

# instance = CLASS()
colors.append("purple")  # colors.append(colors, "purple")
colors.append("chartreuse")
colors.insert(0, "yellow")
print(f"{colors = }")

x = 5    #  shortcut x = int(5)
y = int(10)
print(x * y)

class Dog:
    def bark(self):
        print("woof! woof!")

d1 = Dog()
print(f"{d1 = }")
d1.bark()  #  Dog.bark(d1)

d2 = Dog()
d2.bark()  # Dog.bark(d2)
Dog.bark(d2)
