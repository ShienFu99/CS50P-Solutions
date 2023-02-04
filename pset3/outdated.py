#Description: Prompts the user to input a date in middle-endian order (word form or number form) -> converts to ISO 8601 format
# For word format: Do not abbreviate the name of the month, add a comma after the day, and separate with spaces -> Ie, "September 8, 1636"
# > Day must be between 1 and 31
# For number format: Separate numbers with "/" character -> Ie, "9/8/1636"
# > Month must be between 1 and 12, and day must be between 1 and 31
def main():

    #Run code until user inputs a valid date
    while True:
        #User must input date in month-day-year format (ie, 9/8/1636 or September 8, 1636)
        user_date = input("Date: ").title()

        if validate_word_format(user_date) == False:
            if validate_num_format(user_date) == False:
                #Reprompt user if the date isn't in valid word or number format
                pass
            #Run if date is in proper number format
            else:
                year, month, day = validate_num_format(user_date)
                print(f"{int(year):02}-{int(month):02}-{int(day):02}")
                #Exit loop
                break
        #Run if date is in proper word format
        else:
            year, month, day = validate_word_format(user_date)
            #Needs to print with trailing zeros
            print(f"{int(year):02}-{int(month):02}-{int(day):02}")
            #Exit loop
            break


def validate_word_format(user_date):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    #Checks if the user's date contains one of the months in word format -> If it does, breaks out of loop and replaces the month with it's respective number (September -> 9)
    for i in range(len(months)):
        if months[i] in user_date:
            user_date = user_date.replace(months[i], str(i+1))
            break

    #Checks if the user's string is formatted properly -> If not, return False to main()
    try:
        month, day_year = user_date.split(" ", 1)
        day, year = day_year.split(", ", 1)
    except ValueError:
        return False

    #Checks if the day is valid -> If not, return False to main()
    try:
        if int(day) > 31 or int(day) <= 0:
            raise ValueError
    except ValueError:
        return False

    #If all conditions are met, returns the year, month, and day to main() as a tuple
    return (year, month, day)


def validate_num_format(user_date):
    #Checks if the user's string is formatted properly -> If not, return False to main()
    try:
        month, day, year = user_date.split("/", 2)
    except ValueError:
        return False

    #Checks if the day and month are valid -> If not, return False to main()
    try:
        if int(day) > 31 or int(day) <= 0:
            raise ValueError
        if int(month) > 12 or int(month) <= 0:
            raise ValueError
    except ValueError:
        return False

    #If all conditions are met, returns the year, month, and day to main() as a tuple
    return (year, month, day)


main()
