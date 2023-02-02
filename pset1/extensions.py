#Description: Prompts the user for the name of a file and then outputs that file’s media type if accepted -> If extension is not accepted or present, the program outputs the default media type
def main():
    filename = input("File name: ")

    #If filename does not contain a period
    if filename.find(".") == -1:
        print("application/octet-stream")
    else:
        name, ext_name = filename.split(".", 1)
        ext = "." + ext_name.lower()

        match ext:
            case ".jpg" | ".jpeg" | ".gif" | ".png":
                print("image/" + ext_name.lower())
            case ".pdf" | ".zip":
                print("application/" + ext_name.lower())
            case ".txt":
                print("text/plain")
            case _:
                print("application/octet-stream")

main()
