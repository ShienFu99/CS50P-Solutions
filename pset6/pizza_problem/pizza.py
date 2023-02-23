#Imports
import sys
from tabulate import tabulate
import csv


def main():
    menu = []

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if sys.argv[1].endswith(".csv") == False:
        sys.exit("Not a CSV file")

    try:
        file = open(sys.argv[1], "r")
    except FileNotFoundError:
        sys.exit("File does not exist")

    reader = csv.reader(file, quotechar=",")
    for row in reader:
        menu.append(row)

    print(tabulate(menu[1:], menu[0], tablefmt="grid"))

    file.close()


if __name__ == "__main__":
    main()
