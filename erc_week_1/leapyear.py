
def check_leap_year(year):
    istrue = (year % 4 == 0)

    if (istrue):
        return "The year %s is a leap year!" % year

    if (not istrue):
        return "The year %s is not a leap year." % year

year = int(input("Enter the year: "))

print(check_leap_year(year))
