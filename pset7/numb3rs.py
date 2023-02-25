#Imports
import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"(-?[0-9]+)\.(-?[0-9]+)\.(-?[0-9]+)\.(-?[0-9]+)", ip):
        for i in range(4):
            if int(matches.group(i+1)) not in range(256):
                return False
        return True
    return False


if __name__ == "__main__":
    main()
