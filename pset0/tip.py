#Prompts user for the price of a meal and the percentage they would like to tip -> Tells user how much to tip
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


#Takes a string in $##.## format and returns it as a float without the "$"
#$25.55 -> 25.55
def dollars_to_float(d):
    return float(d.replace("$", ""))


#Takes a string in ##% format and returns it as a float without the "%"
#25% -> 0.25
def percent_to_float(p):
    return float("0." + p.replace("%", ""))


main()
