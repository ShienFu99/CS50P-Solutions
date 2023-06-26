#Imports
import pytest
import unittest
from seasons import Date


class TestDateInit(unittest.TestCase):
    def test_date_init_default(self):
        #The function expects 3 positional arguments as either ints or numbers as strings -> year, month, day
        with pytest.raises(TypeError):
            date = Date()


    def test_date_init_custom(self):
        date = Date("1", "1", "1")
        assert date.year == 1
        assert date.month == 1
        assert date.day == 1

        #The upper limit for days per month changes depending on the month
        # -> February can have either 28 or 29 days depending on if it's a leap year
        date = Date(2024, 1, 31)
        assert date.month == 1
        assert date.day == 31

        date = Date(2023, 2, 28)
        assert date.year == 2023
        assert date.month == 2
        assert date.day == 28

        date = Date(2024, 2, 29)
        assert date.year == 2024
        assert date.month == 2
        assert date.day == 29

        date = Date(2024, 3, 31)
        assert date.month == 3
        assert date.day == 31

        date = Date(2024, 4, 30)
        assert date.month == 4
        assert date.day == 30

        date = Date(2024, 5, 31)
        assert date.month == 5
        assert date.day == 31

        date = Date(2024, 6, 30)
        assert date.month == 6
        assert date.day == 30

        date = Date(2024, 7, 31)
        assert date.month == 7
        assert date.day == 31

        date = Date(2024, 8, 31)
        assert date.month == 8
        assert date.day == 31

        date = Date(2024, 9, 30)
        assert date.month == 9
        assert date.day == 30

        date = Date(2024, 10, 31)
        assert date.month == 10
        assert date.day == 31

        date = Date(2024, 11, 30)
        assert date.month == 11
        assert date.day == 30

        date = Date(2024, 12, 31)
        assert date.month == 12
        assert date.day == 31


    def test_date_init_improper(self):
        with self.assertRaises(SystemExit):
            #Month cannot be between 1 and 12
            date = Date(2023, 0, 5)

        with self.assertRaises(SystemExit):
            date = Date(2023, 13, 5)

        with self.assertRaises(SystemExit):
            #Day must be between 0 and 31 (max, but not all months can equal 31)
            date = Date(2023, 2, 0)

        with self.assertRaises(SystemExit):
            date = Date(2023, 2, 32)

        with self.assertRaises(SystemExit):
            #Year must be a positive integer
            date = Date(0, 2, 2)

        with self.assertRaises(SystemExit):
            date = Date(0.2, 0.2, 0.2)


    def test_date_get_birthdate_default(self):
        with self.assertRaises(AttributeError):
            date = Date.get_birthdate(lambda *args: None)


    def test_date_get_birthdate_custom(self):
        date = Date.get_birthdate(lambda: "2023-2-3")
        assert date.year == 2023
        assert date.month == 2
        assert date.day == 3

        #The upper limit for days per month changes depending on the month
        # -> February can have either 28 or 29 days depending on if it's a leap year
        date = Date.get_birthdate(lambda: "2024-1-31")
        assert date.month == 1
        assert date.day == 31

        date = Date.get_birthdate(lambda: "2023-2-28")
        assert date.year == 2023
        assert date.month == 2
        assert date.day == 28

        date = Date.get_birthdate(lambda: "2024-2-29")
        assert date.year == 2024
        assert date.month == 2
        assert date.day == 29

        date = Date.get_birthdate(lambda: "2024-3-31")
        assert date.month == 3
        assert date.day == 31

        date = Date.get_birthdate(lambda: "2024-4-30")
        date = Date(2024, 4, 30)
        assert date.month == 4
        assert date.day == 30

        date = Date.get_birthdate(lambda: "2024-5-31")
        date = Date(2024, 5, 31)
        assert date.month == 5
        assert date.day == 31

        date = Date.get_birthdate(lambda: "2024-6-30")
        date = Date(2024, 6, 30)
        assert date.month == 6
        assert date.day == 30

        date = Date.get_birthdate(lambda: "2024-7-31")
        date = Date(2024, 7, 31)
        assert date.month == 7
        assert date.day == 31

        date = Date.get_birthdate(lambda: "2024-8-31")
        date = Date(2024, 8, 31)
        assert date.month == 8
        assert date.day == 31

        date = Date.get_birthdate(lambda: "2024-9-30")
        date = Date(2024, 9, 30)
        assert date.month == 9
        assert date.day == 30

        date = Date.get_birthdate(lambda: "2024-10-31")
        date = Date(2024, 10, 31)
        assert date.month == 10
        assert date.day == 31

        date = Date.get_birthdate(lambda: "2024-11-30")
        date = Date(2024, 11, 30)
        assert date.month == 11
        assert date.day == 30

        date = Date.get_birthdate(lambda: "2024-12-31")
        date = Date(2024, 12, 31)
        assert date.month == 12
        assert date.day == 31


    def test_date_get_birthdate_improper(self):
        with self.assertRaises(SystemExit):
            #Input should be in YYYY-MM-DD
            date = Date.get_birthdate(lambda: "January 1, 2023")

        #Month must be between 1 and 12
        with self.assertRaises(SystemExit):
            date = Date.get_birthdate(lambda: "2023-0-5")

        with self.assertRaises(SystemExit):
            date = Date.get_birthdate(lambda: "2023-13-5")

        #Day must be between 1 and 31
        with self.assertRaises(SystemExit):
            date = Date.get_birthdate(lambda: "2023-2-0")

        with self.assertRaises(SystemExit):
            date = Date.get_birthdate(lambda: "2023-2-32")


    def test_date_sub_proper(self):
        #Born on current day
        date_minuend = Date(2024, 1, 31)
        date_subtrahead = Date(2024, 1, 31)
        minutes_since_birth = date_minuend - date_subtrahead
        assert minutes_since_birth == 0

        #One year - regular year
        date_minuend = Date(2023, 1, 1)
        date_subtrahead = Date(2022, 1, 1)
        minutes_since_birth = date_minuend - date_subtrahead
        assert minutes_since_birth == 525600

        #One year - leap year (should add 1 extra day's worth of minutes)
        date_minuend = Date(2021, 1, 1)
        date_subtrahead = Date(2020, 1, 1)
        minutes_since_birth = date_minuend - date_subtrahead
        assert minutes_since_birth == 527040

        #One day
        date_minuend = Date(2021, 1, 2)
        date_subtrahead = Date(2021, 1, 1)
        minutes_since_birth = date_minuend - date_subtrahead
        assert minutes_since_birth == 1440

        #Thirty years
        date_minuend = Date(2020, 1, 1)
        date_subtrahead = Date(1990, 1, 1)
        minutes_since_birth = date_minuend - date_subtrahead
        assert minutes_since_birth == 15778080

        #Corner cases
        date_minuend = Date(2023, 5, 25)
        date_subtrahead = Date(2000, 7, 4)
        minutes_since_birth = date_minuend - date_subtrahead
        assert minutes_since_birth == 12038400

        date_minuend = Date(2020, 1, 6)
        date_subtrahead = Date(2019, 7, 8)
        minutes_since_birth = date_minuend - date_subtrahead
        assert minutes_since_birth == 262080

        date_minuend = Date(2020, 3, 1)
        date_subtrahead = Date(2019, 7, 8)
        minutes_since_birth = date_minuend - date_subtrahead
        assert minutes_since_birth == 341280

        date_minuend = Date(2019, 3, 1)
        date_subtrahead = Date(2018, 7, 8)
        minutes_since_birth = date_minuend - date_subtrahead
        assert minutes_since_birth == 339840


    #__sub__ expects two objects of the type "Date"
    def test_date_sub_improper(self):
        with pytest.raises(AttributeError):
            date_minuend = Date(2024, 1, 31)
            minutes_since_birth = date_minuend - 5

        #User cannot be born at a date that comes after the current date
        with self.assertRaises(SystemExit):
            date_minuend = Date(2023, 0, 5)
            date_subtrahead = Date(2024, 0, 5)
            minutes_since_birth = date_minuend - date_subtrahead

        with self.assertRaises(SystemExit):
            date_minuend = Date(2023, 1, 5)
            date_subtrahead = Date(2023, 1, 6)
            minutes_since_birth = date_minuend - date_subtrahead
