#Description: This program prompts the user to answer the Great Question of Life, the Universe and Everything -> Verifies legitimacy of answer
def main():
    answer_to_universe = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower()

    match answer_to_universe:
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")


main()
