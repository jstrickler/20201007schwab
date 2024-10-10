
g = globals()
person = "Abe Lincoln"
animal = "moose"

def spam():
    print("SPAM SPAM")

print(f"{g = }\n")
print(f"{g['animal'] = }")

g['spam']()
