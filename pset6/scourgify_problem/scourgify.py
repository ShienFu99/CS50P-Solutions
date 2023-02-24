# TO RUN PROGRAM: python lines.py before.csv *NEW FILENAME*
#Description: Reads data from before.csv and reformats it in a new file -> splits name into first and last


#Imports
import sys
import csv


def main():

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if sys.argv[1].endswith(".csv") == False or sys.argv[2].endswith(".csv") == False:
        sys.exit("Not a CSV file")

    try:
        file = open(sys.argv[1], "r")
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    file2 = open(sys.argv[2], "w")

    reader = csv.DictReader(file)
    fieldnames = ["first", "last", "house"]
    writer = csv.DictWriter(file2, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        #Try-except statement removed -> "Assume that each student will have both a first name and last name."
        last, first = row["name"].split(", ", 1)
        writer.writerow({"first": first, "last": last, "house": row["house"]})

    file.close()
    file2.close()


if __name__ == "__main__":
    main()
