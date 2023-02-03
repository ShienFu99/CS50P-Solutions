#Description: Prompts the user for items to add to their grocery list -> If the item is not already on the list, it is added as a new entry
# > If an item appears multiple times, it is listed once with its respective quantity
# > User can quit program by inputting control-d
def main():
    grocery_list = {}

    while True:
        try:
            grocery_item = input().upper()
        except EOFError:
            break

        if grocery_item not in grocery_list:
            grocery_list.update({grocery_item: 1})
        else:
            grocery_list[grocery_item] += 1
        #grocery_list["quantity"] += 1

    for item in sorted(grocery_list):
        print(grocery_list[item], item)

main()
