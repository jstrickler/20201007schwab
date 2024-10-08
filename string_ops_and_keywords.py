a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(f"{c = }\n")

print(f"{a * 5 = }\n")

flags = [0] * 10
print(f"{flags = }\n")

flags = [True] * 20
print(f"{flags = }\n")

colors = ['red', 'green', 'purple', 'orange', 'brown',
'black', 'olive', 'navy', 'white', 'black',
'pink', 'chartreuse']

del colors[0]
del colors[-1]
del colors[4]
print(f"{colors = }\n")

print(f"{'pink' in colors = }")
print(f"{'yellow' in colors = }")


