#Description: Prompts the user for an arithmetic expression, solves it, and then outputs the solution rounded to 1 decimal place
def main():
    expression = input("Expression: ")

    operator1, operand, operator2 = expression.split(" ", 2)

    match operand:
        case "+":
            print(f"{int(operator1) + int(operator2):.1f}")
        case "-":
            print(f"{int(operator1) - int(operator2):.1f}")
        case "*":
            print(f"{int(operator1) * int(operator2):.1f}")
        case "/":
            print(f"{int(operator1) / int(operator2):.1f}")
        case "%":
            print(f"{int(operator1) % int(operator2):.1f}")


main()
