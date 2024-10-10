# define function
def say_hello():
    print("Hello, world")

say_hello()  # Call function

say_hello()
say_hello()
print('-' * 60)

#         xxxx
def greet(whom="world"):
    # if not isinstance(whom, str):
    #    raise TypeError(...)
    print(f"Hello, {whom}")

greet("world")
greet("Schwabbies")

greet()
greet([1,2,3])
