import sys

search_term = sys.argv.pop(1)  # grab 1st arg after script name and remove it

for file_path in sys.argv[1:]:
    print(file_path, "\n")
    with open(file_path) as file_in:
        for raw_line in file_in:
            if search_term in raw_line:
                line = raw_line.rstrip()
                print(line)
    print('-' * 60)
    
