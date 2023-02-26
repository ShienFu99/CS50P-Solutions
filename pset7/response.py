from validator_collection import validators


def main():
    email = input("What's your email? ").strip()

    if validators.email(email):
        print("Valid.")
    else:
        print("Invalid.")


if __name__ == "__main__":
    main()
