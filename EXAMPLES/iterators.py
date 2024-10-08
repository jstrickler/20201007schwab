phrase = ('dog', 'bites', 'man')
print(" ".join(reversed(phrase)))  # reversed() returns a reversed iterator
print()

first_names = "Bill Bill Dennis Steve Larry".split()
last_names = "Gates Joy Richie Jobs Ellison".split()
print(f"{first_names = }")
print(f"{last_names = }")

full_names = zip(first_names, last_names)  # zip() returns an iterator of tuples created from corresponding elements
print("full_names:", full_names)
print()

for first_name, last_name in full_names:
    print(f"{first_name} {last_name}")
print()
print(f"{list(zip(first_names, last_names)) = }")
