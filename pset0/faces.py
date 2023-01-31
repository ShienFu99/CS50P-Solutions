#Takes a message from the user and converts :) and :( to their respective emojis

def main():
    message_after = convert(input("Message: "))
    print(message_after)

def convert(message):
    message = message.replace(":)", "🙂")
    return message.replace(":(", "🙁")

main()
