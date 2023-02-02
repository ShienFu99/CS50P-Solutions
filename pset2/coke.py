#Description: Prompts the user to input coins until they pay 50 cents or more -> Calculates and displays change owed
#Accepted coin: Quarters, dimes, nickels
def main():
    total = 0

    while total < 50:
        print("Amount Due:", 50 - total)
        coin = int(input("Insert Coin: "))

        if coin / 25 == 1:
            total += 25
        elif coin / 10 == 1:
            total += 10
        elif coin / 5 == 1:
            total += 5
        else:
            pass

    print("Change:", total - 50)

main()
