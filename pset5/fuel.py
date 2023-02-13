#Description: Prompts the user for a fuel ratio -> Displays percentage unless tank is full or empty


#Imports
from decimal import Decimal, ROUND_HALF_UP


def main():
    fuel_ratio = input("Fuel: ")
    fuel_percentage = convert(fuel_ratio)
    print(gauge(fuel_percentage))


def convert(fraction):

    #If there is no "/" in the user's ratio, the function will trigger a ValueError
    X, Y = fraction.split("/", 1)
    #If X or Y are not numbers, they cannot be converted to integers -> causes a ValueError
    X, Y = int(X), int(Y)
    #X and Y cannot be negative as you cannot have negative fuel, and X cannot be greater than Y as you cannot have more than 100% fuel
    if X > Y or X < 0 or Y < 0:
        raise ValueError
    #If Y is 0, it will eventually lead to a ZeroDivisionError
    elif Y == 0:
        raise ZeroDivisionError

    #Python rounds number inconsistently, so the decimal library was used to make it more consistent -> Always rounds up at 0.5
    return int(Decimal(str((X/Y) * 100)).quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{int(percentage)}%"


if __name__ == "__main__":
    main()
