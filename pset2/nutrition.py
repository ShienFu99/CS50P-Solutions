#Description: Prompts user for an item -> If it's fruit from the FDA's poster, the associated number of calories are displayed
def main():

    fruit_list = {
        "Apple": "130",
        "Avocado": "50",
        "Banana": "110",
        "Cantaloupe": "50",
        "Grapes": "90",
        "Honeydew Melon": "50",
        "Kiwifruit", "90",
        "Lemon": "15",
        "Lime": "20",
        "Nectarine": "60",
        "Orange": "80",
        "Peach": "60",
        "Pear": "100",
        "Pineapple": "50",
        "Plums": "70",
        "Strawberries": "50",
        "Sweet Cherries": "100",
        "Tangerine": "50",
        "Watermelon": "80"
    }

    user_fruit = input("Item: ").title()

    if user_fruit in fruit_list:
        print("Calories:", fruit_list[user_fruit])

main()
