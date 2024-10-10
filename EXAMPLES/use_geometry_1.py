import sys
import geometry # find geometry.py and run 
#       pkg     pkg   module
import django.contrib.auth  # find django/contrib/auth.py

a1 = geometry.circle_area(8)
a2 = geometry.rectangle_area(10, 12)
a3 = geometry.square_area(7.9)
print(a1, a2, a3)

# module/package search algorithm
# 1. current folder
# 2. folders in PYTHONPATH if it exists
# 3. installation folder + "lib"  (sys.prefix + "lib")

print(f"{sys.prefix = }")
print()
for path in sys.path:
    print(path)
