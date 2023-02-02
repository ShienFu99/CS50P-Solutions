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
            X, Y = fuel_ratio.split("/", 1)
            X, Y = int(X), int(Y)
            if X > Y or X < 0 or Y <= 0:
                raise ValueError
            return fuel_ratio
        except ValueError:
            pass


def calculate_percentage(fuel_ratio):
    X, Y = fuel_ratio.split("/", 1)
    return int(X)/int(Y) * 100


main()
