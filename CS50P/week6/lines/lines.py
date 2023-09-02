import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not (sys.argv[1].endswith(".py")):
        sys.exit("Not a Python file")

    try:
        print(count_lines(sys.argv[1]))
    except FileNotFoundError:
        sys.exit("File does not exist")

def is_valid_extension(name):
    if name.endwith(".py"):
        return True
    else:
        return False

def count_lines(file_name):
    c = 0
    with open(file_name) as file:
        for line in file:
            c = c + 1
            if line.strip().startswith("#"):
                c = c - 1
            if len(line.strip()) == 0:
                c = c -1
    return c

if __name__ == "__main__":
    main()