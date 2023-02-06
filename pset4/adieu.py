#Descriptions: Prompts user for names until they exit using control-d -> Bids adieu in a grammatically correct fashion


#Imports
import inflect


def main():

    names = []
    p = inflect.engine()

    while True:
        try:
            name = input("Name: ").capitalize()
        except EOFError:
            print()
            break
        names.append(name)

    print("Adieu, adieu, to", p.join(names))


if __name__ == "__main__":
    main()
