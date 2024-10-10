from timeit import Timer

STARTUP = """
import os
FOLDER = "DATA"
"""

snippet1 = """
names = []
for file_name in os.listdir(FOLDER):
    names.append(file_name)
"""

snippet2 = """
names = []
for file_entry in os.scandir(FOLDER):
    names.append(file_entry.name)
"""

timer1 = Timer(snippet1, STARTUP)
timer2 = Timer(snippet2, STARTUP)

print(timer1.timeit(100000))
print(timer2.timeit(100000))



