#Description: Prompts user for a difficulty level -> Generates 10 addition equations based on the user's difficulty level
# > Level determines number of digits each operand can have per addition equation
# > User gets 3 tries per equation
# > Final score is tallied out of 10
# Program has basic error checking


#Imports
import random


def main():

    user_score = 0
    user_level = get_level()

    #Generates 10 addition equations for the user to solve
    for _ in range(10):
        equation = f"{generate_integer(user_level)} + {generate_integer(user_level)}"
        operand1, operand2 = equation.split(" + ", 1)
        solution = int(operand1) + int(operand2)

        #User has 3 tries -> Each wrong/invalid guess causes them to lose an attempt
        #If all 3 guesses are wrong, the correct solution is displayed
        user_tries = 3
        while user_tries > 0:
            print(equation + " = ", end="")

            try:
                user_answer = int(input())
                if user_answer != solution:
                    raise ValueError
            except ValueError:
                print("EEE")
                user_tries -= 1
            else:
                user_score += 1
                break
        if user_tries == 0:
            print(f"{equation} = {solution}")

    #Displays final score
    print("Score:", user_score)


def get_level():
    #user_level must be 1, 2, or 3
    while True:
        try:
            user_level = int(input("Level: "))
            if user_level in [1, 2, 3]:
                return user_level
        except ValueError:
            pass


def generate_integer(level):

    #As per the instructions, if the level is not 1, 2, or 3, a ValueError is raised
    if level not in [1, 2, 3]:
        raise ValueError

    #level -> number of digits for each operand
    if level == 1:
        return f"{random.randint(0, 9)}"
    if level == 2:
        return f"{random.randint(10, 99)}"
    if level == 3:
        return f"{random.randint(100, 999)}"


if __name__ == "__main__":
    main()
