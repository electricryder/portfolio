import sys
import csv
from tabulate import tabulate


def main():
    chosen_file = valid_arg()
    table = formated_pizza_table(chosen_file)
    print(table)


def valid_arg():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            pizza_type = sys.argv[1]
    try:
        with open(pizza_type) as file:
            return sys.argv[1]
    except FileNotFoundError:
        sys.exit("File does not exist")


def formated_pizza_table(pizzafile):

    pizza_table = []

    with open(pizzafile) as file:
        reader = csv.DictReader(file)
        for row in reader:
            pizza_table.append(row)

        return tabulate(pizza_table, headers="keys", tablefmt="grid")


if __name__ == "__main__":
    main()
