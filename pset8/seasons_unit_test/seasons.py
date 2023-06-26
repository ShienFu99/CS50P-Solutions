#Imports
import sys
from datetime import date
import inflect


class Date:
    #Binds each month to its respective amount of days
    days_per_month = {1:31,
                     2:28,
                     3:31,
                     4:30,
                     5:31,
                     6:30,
                     7:31,
                     8:31,
                     9:30,
                     10:31,
                     11:30,
                     12:31}


    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


    @property
    def year(self):
        return self._year


    @year.setter
    def year(self, year):
        #Raises a ValueError if the year isn't a positive integer -> Exits program with error message
        try:
            year = int(year)
            if year < 1:
                raise ValueError
        except ValueError:
            sys.exit("Invalid date")
        self._year = year


    @property
    def month(self):
        return self._month


    @month.setter
    def month(self, month):
        #Raises a ValueError if the month inputted is invalid (not between 1 and 12)
        try:
            month = int(month)
            if month < 1 or month > 12:
                raise ValueError
        except ValueError:
            sys.exit("Invalid date")
        self._month = month


    @property
    def day(self):
        return self._day


    @day.setter
    def day(self, day):
        try:
            day = int(day)
            #Raises ValueError if day isn't a positive integer
            if day < 1:
                raise ValueError

            #The upper limit for the day depends on the month
            # -> If the month isn't February, then it's the number of days in the respective month
            # -> If the month is February, then it can be 28 or 29 depending on if it's a leap year
            #Failure to comply with the upper limit raises a ValueError
            if self.month == 2 and type(Date.is_leapyear(self.year)) == bool:
                if day > 29:
                    raise ValueError
            elif self.month == 2:
                if day > 28:
                    raise ValueError
            else:
                if day > Date.days_per_month[self.month]:
                    raise ValueError

        except ValueError:
            sys.exit("Invalid date")
        self._day = day


    #Method tells if the inputted year is a leap year (in which case it returns True) -> If not, it returns the number of years until the next leap year
    @classmethod
    def is_leapyear(cls, year):
        #If the year is evenly divisible by 100, it must also be evenly divisible by 400 to be a leap year -> 400 is a leap year, but 100 is not
        if year % 100 == 0 and year % 400 == 0:
            return True
        #If the previous condition isn't met, all years evenly divisible by 4 but not by 100 are considered leap years
        elif year % 4 == 0 and year % 100 != 0:
            return True
        #If none of the conditions above are met, then the current year isn't a leap year
        else:
            #For years evenly divisible by 100 but not 400, the next leap year is in 4 years
            if year % 4 == 0:
                return 4
            #For years not evenly divisible by 4, the next leap year is between 1 and 3 years away -> Ie, for 2022, the next leap year is in 2 years
            else:
                return 4 - (year % 4)


    #Used for pytest -> Prompts for birthdate
    def prompt_for_birthdate():
        return input("Date of Birth: ")


    #Method gets a birthdate from the user in YYYY-MM-DD format -> returns a Date object
    @classmethod
    def get_birthdate(cls, prompt_for_birthdate):
        try:
            year, month, day = prompt_for_birthdate().split("-", 2)
        except ValueError:
            sys.exit("Invalid date")
        return Date(year, month, day)


    # ***Used primarily for testing***
    def __str__(self):
        return f"{self.year} year, {self.month} month, {self.day} day."


    #Method allows the user to subtract two Date objects -> returns the number of minutes since the user was born
    def __sub__(self, other):
        days_minuend, days_subtrahead, day_diff = 0, 0, 0

        #If the user's birth year is greater than the current year, exit program
        if other.year > self.year:
            sys.exit("Invalid date")
        #If the user's birth year matches the current year, calculate the total number of days elapsed in the current year and the user's birth year, then subtract them
        # -> If more days have elapsed in the birth year, the user hasn't been born yet -> Exit program
        # -> If not, then the difference is passed to the end of the function, where it is converted into minutes and returned
        elif other.year == self.year:
            #Accounts for extra day if the current year is a leap year
            if type(Date.is_leapyear(self.year)) == bool:
                if self.month >= 3:
                    days_minuend += 1
                if other.month >= 3:
                    days_subtrahead += 1

            #Adds days in current month
            days_minuend += self.day
            days_subtrahead += other.day

            #Adds days from each month leading up to the current month
            for i in range(self.month-1):
                days_minuend += Date.days_per_month[i+1]

            for i in range(other.month-1):
                days_subtrahead += Date.days_per_month[i+1]

            if days_subtrahead > days_minuend:
                sys.exit("Invalid date")
            elif days_subtrahead == days_minuend:
                #Nothing needs to be done as day_diff is already initialized at 0
                pass
            else:
                day_diff = days_minuend - days_subtrahead

        #The else-branch is run if the user was born 1 or more years before the current year
        else:
            #Adds remaining days in current month (ie, if it's the 5th of January, remaining days = 26)
            #Accounts for leap years by adding an extra day for February
            if other.month <= 2 and type(Date.is_leapyear(other.year)) == bool:
                day_diff += (Date.days_per_month[other.month] + 1) - other.day
            else:
                day_diff += Date.days_per_month[other.month] - other.day

            #Adds days in remaining months
            for i in range(12-other.month):
                day_diff += Date.days_per_month[i+1+other.month]
            other.year += 1

            #At this point, the day_diff accounts for all of the days in the given birth year

            #Adds number of days per year until the birth year matches the current year
            #Accounts for leap years
            while other.year != self.year:
                if type(Date.is_leapyear(other.year)) == bool:
                    day_diff += 366
                else:
                    day_diff += 365
                other.year += 1

            #Add days per month leading up to current one + self.day
            for i in range(self.month-1):
                day_diff += Date.days_per_month[i+1]

            #Determines if another day must be added based on whether it's a leap year and enough time has passed
            if type(Date.is_leapyear(other.year)) == bool and self.month != 2 and self.month >= 3:
                day_diff += 1

            #Has the potential to add 29 instead of 28
            day_diff += self.day

        #Returns number of minutes user has been alive for under given conditions
        return day_diff * 24 * 60


def main():
    p = inflect.engine()

    #Prompts the user for their birthdate - Saves as an object
    Birthdate = Date.get_birthdate(Date.prompt_for_birthdate)

    #Gets current date and makes it an object of Date class for compatibility
    year_today, month_today, day_today = str(date.today()).split("-", 2)
    date_today = Date(int(year_today), int(month_today), int(day_today))

    #Subtracts the current date by the user-inputted birthdate -> Value stored is the number of minutes the user has been alive
    minutes_since_birth = date_today - Birthdate

    #Prints the number of minutes the user has been alive
    print(p.number_to_words(minutes_since_birth, andword="").capitalize(), "minutes")


if __name__ == "__main__":
    main()
