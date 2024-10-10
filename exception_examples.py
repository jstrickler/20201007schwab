import sys

FILE_PATH = "junk/weaseldust.txt"

try:
    with open(FILE_PATH) as file_in:
        for line in file_in:
            print(line.rstrip())
except (FileNotFoundError, NotADirectoryError)  as err:
    print(err, file=sys.stderr)
except PermissionError as err:
    print("Whoa!", err, file=sys.stderr)
except Exception as err:
    print("Did not expect", err)

print("ALL DONE")
