from argparse import ArgumentParser

parser = ArgumentParser(description="Sample script with named arguments")

# change "+" to "*" to allow zero arguments
parser.add_argument("raw_args", metavar="key=value", nargs="+", help="Arguments of form name=value")

args = parser.parse_args()
print(f"{args = }\n")

print(f"args.raw_args = {args.raw_args}\n")


# process key=value pairs from command line
named_args = {}
for arg in args.raw_args:
    key, value = arg.split('=')
    named_args[key] = value
print(f"{named_args = }\n")

# short version
# named_args = {key:value for key, value in (arg.split('=') for arg in args.raw_args)}
    
# list of args as tuples
named_args_tuples = [tuple(arg.split('=')) for arg in args.raw_args]
print(f"{named_args_tuples = }\n")

