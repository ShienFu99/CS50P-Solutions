#Prompts user for a mass in kg and prints the equivalent number of Joules using the formula E=mc^2
mass = int(input("m (kg): "))
c = 300000000
print(f"E: {mass*c**2}")
