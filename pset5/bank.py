#Description: Prompts user for greeting and displays money owed depending on how proper it is
def main():
    user_greeting = input("Greeting: ")

    print("$" + str(value(user_greeting)))


def value(greeting):

    greeting = greeting.strip().lower()

    if greeting.startswith("hello"):
        return(0)
    elif greeting.startswith("h"):
        return(20)
    else:
        return(100)


if __name__ == "__main__":
    main()
