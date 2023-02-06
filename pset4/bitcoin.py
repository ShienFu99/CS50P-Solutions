#Description: Number of bitcoins inputted by user gets converted to USD_conversion
# Expects 1 command-line argument, being the number of bitcoins
# Program has basic error checking


#Imports
import requests
import sys
import json


def main():

    #There must be 1 additional command-line argument (number of bitcoins to convert)
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line argument")

    #The bitcoin amount must be convertable to float
    try:
        bitcoin_amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    #Tries to reach the link and retrieve a JSON file
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit("Unable to reach server")

    #Converts to JSON
    o = response.json()

    #Calculates the bitcoin's value in USD and prints it to four decimal places
    result = o["bpi"]
    result_USD = result["USD"]
    USD_conversion = result_USD["rate_float"] * bitcoin_amount

    #Future improvement: result = o["bpi"]["USD"]["rate_float"]

    print(f"${USD_conversion:,.4f}")


if __name__ == "__main__":
    main()
