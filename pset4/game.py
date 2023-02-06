#Description: The user is prompted for a number -> A secret number is generated between 1 and their number (inclusive) -> The user has to guess the number
# > Program has basic error checking


#Imports
import random
import sys


def main():

    #user_level must be a positive integer
    while True:
        try:
            user_level = int(input("Level: "))
            if user_level > 0:
                break
        except ValueError:
            pass


    #Generates a random number between 1 and user_level (inclusive)
    secret_num = random.randint(1, user_level)

    #Double while-loop allows for break statement to be used to retrigger inner while-loop (since program ends with sys.exit())
    while True:
        #Reprompts user until they guess the secret number
        while True:
            try:
                user_guess = int(input("Guess: "))
                if user_guess <= 0:
                    raise ValueError
            except ValueError:
                break

            if user_guess < secret_num:
                print("Too small!")
            elif user_guess > secret_num:
                print("Too large!")
            else:
                sys.exit("Just right!")


if __name__ == "__main__":
    main()
