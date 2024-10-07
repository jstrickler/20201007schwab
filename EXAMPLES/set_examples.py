
set1data = ['red', 'blue', 'green', 'purple', 'green']  # create literal set
set2data = ['green', 'blue', 'yellow', 'orange']

set1 = set(set1data)
set2 = set(set2data)

set1.add('taupe')  # add element to set (ignored if already in set)

print(f"{set1 = }")
print(f"{set2 = }")
print(f"{set1 & set2 = }")  # intersection -- common items
print(f"{set1 ^ set2 = }")  # XOR -- non-common items (in one set but not both)
print(f"{set1 | set2 = }")  # union -- unique combination of both sets
print(f"{set1 - set2 = }")  # difference -- Remove items in right set from left set
print(f"{set2 - set1 = }")
print()

with open('../DATA/breakfast.txt') as breakfast_in:
    food = breakfast_in.read().splitlines()

print(f"{food = }")
print()

unique_food = set(food)  # Create set from iterable (e.g., list)
print(f"{unique_food = }")
