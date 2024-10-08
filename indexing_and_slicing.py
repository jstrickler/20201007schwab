fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

print(f"{fruits[0] = }")
print(f"{fruits[8] = }")
print(f"{fruits[len(fruits)-1] = }")
print(f"{fruits[-1] = }")

index = 14
print(f"{fruits[index] = }")
print()
print(f"{fruits = }\n")

#   start-at:stop-before:count-by
print(f"{len(fruits) = }")
print(f"{fruits[0:4] = }")
print(f"{fruits[:4] = }")
print(f"{fruits[13:] = }")
print(f"{fruits[4:7] = }")
print(f"{fruits[::] = }")
print(f"{fruits[::2] = }")

print(f"{fruits[-5:] = }")
print(f"{fruits[1:-1] = }") # omit first and last elements
# print(f"{fruits[1:-1] = }") # omit first and last elements
print()

t = "Taylor Swift"
print(f"{t = }")
print("t is", t)
print(f"{t = !s}")


print(f"{t[:3]}-{t[:3]}")
print(f"{t[:6] = }")
print(f"{t[-5:] = }")
print()

fruits_copy = fruits[1:-1]
print(f"{fruits_copy = }")
print()

with open("somefruits.txt", "w") as fruits_out:
    for fruit in fruits:
        # fruit = ...next value of fruits list...
        fruits_out.write(fruit + "\n")

for fruit in fruits:
    if fruit.lower().startswith('p'):
        print(fruit.upper())
print()

x = "abc"
for chr in x:
    print(chr)
print('-' * 60)

for fruit in fruits:
    print(fruit.title())
    if fruit == 'fig':
        break
