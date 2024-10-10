import typing as T
from EXAMPLES.geometry import circle_area

result: str

result = circle_area(45)

print(f"{result = }")

def process_files(file_list: T.Iterable):
    for file_name in file_list:
        print(file_name)

def doit(thing: T.Any):
    pass

# T.Union[list, tuple]
#  list|tuple

funky_list: list[dict[str,float]]


