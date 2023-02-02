#Description: Prompts user for greeting and displays money owed depending on how proper it is
def main():
    user_greeting = input("Greeting: ").strip().lower()

    if user_greeting.startswith("hello"):
        print("$0")
    elif user_greeting.startswith("h"):
        print("$20")
    else:
        print("$100")


main()
