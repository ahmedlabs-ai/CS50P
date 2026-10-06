import sys

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")


try:
    with open(sys.argv[1]) as file:
        total_lines = 0

        for line in file:
            if not line.strip():
                continue
            elif line.strip().startswith("#"):
                continue
            total_lines += 1
        print(total_lines)


except FileNotFoundError:
    sys.exit("File does not exist")
