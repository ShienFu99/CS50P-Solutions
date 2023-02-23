# TO RUN PROGRAM: python lines.py *FILENAME*
# Description: Takes a file name from the user as a command-line argument -> outputs the number of lines of code in that file, excluding comments and blank lines
# > "A docstring should no be considered a comment." -> Docstrings are counted as lines of code
# Note: From my interpretation, a docstring is any multi-line comment that appears in the first line of a module, function, class or method


#Imports
import sys


def main():
    #Exits program if the user inputs an invalid number of command-line arguments
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    #Exits program if the file name does not end with .py
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    #Tries to open file -> Exits if FileNotFoundError occurs
    try:
        file = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File DNE!")

    line_count = count_lines(file)
    print(line_count)

    file.close()


def count_lines(file):
    line_num = 0
    line_count = 0
    docstring_check = False
    first_line = False
    triple_quote = False
    module_docstring_check = False

    for line in file:
        #Increments line_num for each line in the file
        line_num += 1

        #If triple quotes are detected in the first line of the file, there is a docstring that needs to be counted
        #module_docstring_check is set to False by default and becomes true if the condition above is met
        if line_num == 1 and (line.strip().startswith("\"\"\"") or line.strip().startswith("\'\'\'")):
            module_docstring_check = True
            line_count += 1
            #If there is a complete set of triple quotes, the docstring is only 1 line long -> module_docstring_check is set to False
            if line.count("\"\"\"") == 2 or line.count("\'\'\'") == 2:
                module_docstring_check = False
            continue

        #If module_docstring_check is still True, then the docstring is longer than 1 line of code
        #line_count is incremented until the matching set of triple quotes is found -> module_docstring_check is set to False to avoid retriggering the check later
        if module_docstring_check == True:
            line_count += 1
            if line.count("\"\"\"") == 1 or line.count("\'\'\'") == 1:
                module_docstring_check = False
            continue

        #If a line starts with the "class" or "def" keyword, then the following line could be a docstring
        if line.strip().startswith("class") or line.strip().startswith("def"):
            #line_count is incremented to account for the line of code that starts with "class" or "def"
            line_count += 1
            #The following variables are for future checks
            docstring_check = True
            first_line = True
            continue

        #docstring_check and first_line are True, then the current line of code must be checked for a docstring (line after "class"/"def" keyword is detected)
        if docstring_check == True and first_line == True:
            #If the line starts with triple quotes, then there is a docstring
            if line.strip().startswith("\"\"\"") or line.strip().startswith("\'\'\'"):
                #Increment the count by 1
                line_count += 1
                #If a full set of triple quotes is found, the docstring is 1 line long -> Set check to False
                if line.count("\"\"\"") == 2 or line.count("\'\'\'") == 2:
                    docstring_check = False
                #If there is only one instance of triple quotes, first_line is set to False -> Indicates the docstring is longer than 1 line
                else:
                    first_line = False
                continue
            #If the line does not start with triple quotes, docstring_check is set to False to avoid future checks
            else:
                docstring_check = False

        #If docstring_check is still True, then the remaining lines of the docstring are counted until the matching pair of triple quotes is found -> docstring_check is set to False
        if docstring_check == True:
            line_count += 1
            if line.count("\"\"\"") == 1 or line.count("\'\'\'") == 1:
                docstring_check = False
            continue

        #The remaining code is used to avoid counting multi-line comments that are not docstrings
        #If the line starts with triple quotes, triple_quote is set to True -> it gets set to False if a complete set of triple quotes is found
        if line.strip().startswith("\"\"\"") or line.strip().startswith("\'\'\'"):
            triple_quote = True
            if line.count("\"\"\"") == 2 or line.count("\'\'\'") == 2:
                triple_quote = False
            continue

        #If triple_quote is still True, the multi-line comment is longer than 1 line -> it becomes False once the matching pair of triple quotes is found, ending the comment
        if triple_quote == True:
            if line.count("\"\"\"") == 1 or line.count("\'\'\'") == 1:
                triple_quote = False
            continue

        #Any remaining lines of code that aren't whitespace or regular comments (start with #) get added to the count
        if line.isspace() == False and line.strip().startswith("#") == False:
            line_count += 1

    return line_count


if __name__ == "__main__":
    main()
