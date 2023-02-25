#Imports
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    """Converts time in AM/PM format to 24-hour format"""

    if matches := re.search(r"(\d{1,2})(:\d{2})? (AM|PM) to (\d{1,2})(:\d{2})? (AM|PM)", s):
        hour1 = int(matches.group(1))
        if matches.group(2) != None:
            minutes1 = int(matches.group(2).replace(":", ""))
        hour2 = int(matches.group(4))
        if matches.group(5) != None:
            minutes2 = int(matches.group(5).replace(":", ""))

        hour1 = convert_time_period(hour1, matches.group(3))
        hour2 = convert_time_period(hour2, matches.group(6))

        #Depending on whether the user input minutes, the return value changes
        if matches.group(2) != None and matches.group(5) != None:
            if minutes1 > 59:
                raise ValueError
            if minutes2 > 59:
                raise ValueError
            return f"{hour1:02}:{minutes1:02} to {hour2:02}:{minutes2:02}"
        elif matches.group(2) != None:
            if minutes1 > 59:
                raise ValueError
            return f"{hour1:02}:{minutes1:02} to {hour2:02}:00"
        elif matches.group(5) != None:
            if minutes2 > 59:
                raise ValueError
            return f"{hour1:02}:00 to {hour2:02}:{minutes2:02}"
        else:
            return f"{hour1:02}:00 to {hour2:02}:00"
    else:
        raise ValueError


def convert_time_period(hour, period):
    """Converts hours in AM/PM format to 24-hour format"""

    if hour > 12 or hour < 1:
        raise ValueError

    if period == "PM" and hour != 12:
        hour += 12
    elif period == "AM" and hour == 12:
        hour = 0
    return hour


if __name__ == "__main__":
    main()
