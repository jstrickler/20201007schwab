cities = []  # empty list
cities = ['Portland', 'Pittsburgh', 'Peoria']
print(f"cities: {cities}\n")

cities.append('Miami')
cities.append('Montgomery')
print(f"cities: {cities}\n")

cities.insert(0, 'Boston')
cities.insert(5, "Buffalo")
print(f"cities: {cities}\n")

more_cities = ["Detroit", "Des Moines"]
cities.extend(more_cities)  # add elements one at a time
print(f"cities: {cities}\n")

#  LIST.append(obj)  LIST.insert(pos, obj)  LIST.extend(iterable)

del cities[3]
print(f"cities: {cities}\n")

cities.remove('Buffalo')  # remove first matching element
print(f"cities: {cities}\n")

city = cities.pop()
print(f"city: {city}")
print(f"cities: {cities}\n")

city = cities.pop(3)
print(f"city: {city}")
print(f"cities: {cities}\n")
