#Description: Prompts the user for a message and prints it in a random font or the font chosen using pyfiglet
# > If the user inputs zero command-line arguments, the font is selected randomly from the list of fonts
# > If the user inputs two command-line arguments, they can choose the font
# -> First argument must be "-f" or "--font"
# -> Second argument must be a valid font from the font list
# If any of the conditions aren't met, the program will exit with an error message


#Imports
import sys
import random
from pyfiglet import Figlet


def main():

    figlet = Figlet()

    #Get list of fonts
    font_list = figlet.getFonts()

    #Runs if no additional command-line arguments are inputted
    if (len(sys.argv) - 1) == 0:
        user_input = input("Input: ")

        #Selects a random font from the list -> Future improvement: Use choice() function
        figlet.setFont(font=font_list[random.randint(0, len(font_list) - 1)])

        #Renders and prints text using the selected font
        print("Output:\n", figlet.renderText(user_input), sep="")

    #Runs if two additional command-line arguments are inputted
    elif (len(sys.argv) - 1) == 2:

        #First command-line argument must be "-f" or "--font" -> else program exits with error message
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":

            #Second command-line argument must be a valid font from the font_list -> else program exits with error message
            if sys.argv[2] in font_list:
                user_input = input("Input: ")

                #Sets the font based on what was inputted at the command-line
                figlet.setFont(font=sys.argv[2])

                #Renders and prints text using selected font
                print("Output:\n", figlet.renderText(user_input), sep="")
            else:
                sys.exit("Invalid font name.")
        else:
            sys.exit("Argument 1 must be -f or --font")
    else:
        sys.exit("Invalid number of arguments.")


if __name__ == "__main__":
    main()
