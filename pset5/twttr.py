#Description: Prompts the user for a str and outputs the same text with the vowels omitted (case-insensitively)
def main():
    original_tweet = input("Input: ")
    tweet_omit = shorten(original_tweet)
    print("Output:", tweet_omit)


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]

    #Compare each char to each vowel in vowels list (uppercase and lowercase) -> If match is found, split string at vowel and concatenate pre / post to remove the vowel
    for char in word:
        for vowel in vowels:
            if char == vowel or char == vowel.upper():
                if char.isupper() == True:
                    pre, post = word.split(vowel.upper(), 1)
                else:
                    pre, post = word.split(vowel, 1)

                word = pre + post
                break

    return word


if __name__ == "__main__":
    main()
