#Description: Prompts the user for a str and outputs the same text with the vowels omitted (case-insensitively)
def main():
    original_tweet = input("Input: ")
    tweet_omit = omit_vowels(original_tweet)
    print("Output:", tweet_omit)


def omit_vowels(original_tweet):
    vowels = ["a", "e", "i", "o", "u"]

    #Compare each char to each vowel in vowels list (uppercase and lowercase) -> If match is found, split string at vowel and concatenate pre / post to remove the vowel
    for char in original_tweet:
        for vowel in vowels:
            if char == vowel or char == vowel.upper():
                if char.isupper() == True:
                    pre, post = original_tweet.split(vowel.upper(), 1)
                else:
                    pre, post = original_tweet.split(vowel, 1)

                original_tweet = pre + post
                break

    return original_tweet


main()
