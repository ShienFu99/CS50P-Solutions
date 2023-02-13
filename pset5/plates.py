#Description: Prompts user for a license plate and notifies them if it is valid or invalid based on the outlined conditions
#Conditions:
# - Plates must be between 2 and 6 characters long
# - First two characters must be letters
# - Letters cannot appear after numbers
# - Plates cannot contain spaces, punctuation or periods
# - The first number to appear in a plate cannot be 0
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    i = 0

    #Plate must be between 2 and 6 characters long
    if len(s) < 2 or len(s) > 6:
        return False

    #First two chars must be letters
    while i < 2:
        if s[i].isalpha() != True:
            return False
        i += 1

    #Remaining chars must be letters or numbers -> Once a number is detected, break from while-loop
    while i < len(s):
        if s[i].isalpha() != True and s[i].isnumeric() != True:
                return False
        if s[i].isnumeric() == True:
            #First number cannot be 0
            if s[i] == "0":
                return False
            i += 1
            break
        i += 1

    #Remaining characters must be numbers
    while i < len(s):
        if s[i].isnumeric() != True:
            return False
        i += 1

    #Returns True if all conditions are met
    return True


if __name__ == "__main__":
    main()
