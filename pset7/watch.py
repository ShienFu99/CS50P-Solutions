# Description: Extract the URL of a YouTube video from the user-inputted HTML string (ie, https://www.youtube.com/embed/xvFZjo5PgG0) -> Converts it to a shorter, shareable youtu.be URL
# Accepted formats examples:
# http://youtube.com/embed/xvFZjo5PgG0
# http://www.youtube.com/embed/xvFZjo5PgG0
# https://youtube.com/embed/xvFZjo5PgG0
# https://www.youtube.com/embed/xvFZjo5PgG0


#Imports
import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"src=\"(?:https?://)?(?:www\.)?youtube.com/embed/([^ ]+)\"", s, re.IGNORECASE):
        return "https://youtu.be/" + matches.group(1)
    else:
        return None


if __name__ == "__main__":
    main()
