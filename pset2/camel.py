#Description: Prompts user for the name of a variable in camel case -> outputs the corresponding name in snake case
def main():
    camel_case = input("camelCase: ")
    snake_case = camel_case

    for char in camel_case:
        if char.isupper():
            pre, post = camel_case.split(char, 1)
            snake_case = pre + "_" + char.lower() + post
            camel_case = snake_case

    print("snake_case:", snake_case)


main()
