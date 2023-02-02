#Description: Prompts the user for a fuel ratio -> Displays percentage unless tank is full or empty
# *Program has basic error checking
def main():
    fuel_ratio = get_ratio()
    fuel_percentage = calculate_percentage(fuel_ratio)

    if fuel_percentage <= 1:
        print("E")
    elif fuel_percentage >= 99:
        print("F")
    else:
        print(f"{int(fuel_percentage)}%")


def get_ratio():
    while True:
        fuel_ratio = input("Fuel: ")
        try:
            #If there is no "/" in the user's ratio, the function will trigger a ValueError
            X, Y = fuel_ratio.split("/", 1)
            #If X or Y are not numbers, they cannot be converted to integers -> causes a ValueError
            X, Y = int(X), int(Y)
            #X and Y cannot be negative as you cannot have negative fuel, and X cannot be greater than Y as you cannot have more than 100% fuel
            if X > Y or X < 0 or Y < 0:
                raise ValueError
            #If Y is 0, it will eventually lead to a ZeroDivisionError
            elif Y == 0:
                raise ZeroDivisionError
            return fuel_ratio
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


def calculate_percentage(fuel_ratio):
    X, Y = fuel_ratio.split("/", 1)
    return int(X)/int(Y) * 100


main()
