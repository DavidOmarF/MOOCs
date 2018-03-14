# By Ashwath from forums

# A leap year baby is a baby born on Feb 29, which occurs only on a leap year.

# Define a procedure is_leap_baby that takes 3 inputs: day, month and year
# and returns True if the date is a leap day (Feb 29 in a valid leap year)
# and False otherwise.

## Number Number Number -> Boolean
## If year is leap and day == 29 returns true
def is_leap_baby(day,month,year):
    return ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)) and day == 29


# The function 'output' prints one of two statements based on whether 
# the is_leap_baby function returned True or False.

def output(status,name):
    if status:
        print ("%s is one of an extremely rare species. He is a leap year baby!" % name)
    else:
        print ("There's nothing special about %s's birthday. He is not a leap year baby!" % name)