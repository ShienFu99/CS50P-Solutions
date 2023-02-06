#Description: Prompts the user for a message -> If it contains any Emoji codes, it will be converted to its respective emoji (aliases included)


#Imports
import emoji


def main():

    user_message = input("Input: ")

    #Converts the user's message using emojize, once using the default Emoji codes, and then a second time for aliases -> Prints the new message
    print(emoji.emojize(emoji.emojize(f"Output: {user_message}"), language="alias"))


if __name__ == "__main__":
    main()
