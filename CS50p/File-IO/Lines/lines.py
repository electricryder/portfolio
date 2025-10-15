import sys


def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-3:] != ".py":
            sys.exit("Not a Python file")
        else:
            code_file = sys.argv[1]
    try:
        with open(code_file, "r") as file:
            lines_list = file.readlines()
            n_lines = len(lines_list)
    except FileNotFoundError:
        sys.exit("File does not exist")

    for line in lines_list:
        if line.lstrip().startswith("#"):
            n_lines -= 1
    for line in lines_list:
        if line.strip() == "":
            n_lines -= 1

    print(n_lines)


if __name__ == "__main__":
    main()
