#Description: Program prompts user to enter items of the menu and totals their price until they exit using control-d -> Ignores items inputted that aren't on the menu
def main():
    total = 0
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    while True:
        #If user inputs control-d -> Exits while-loop and ends program
        try:
            user_order = input("Item: ").title()
        except EOFError:
            print()
            break

        if user_order in menu:
            total += menu[user_order]
            print(f"Total: ${total:.2f}")


main()
