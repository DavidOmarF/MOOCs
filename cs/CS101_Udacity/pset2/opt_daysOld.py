# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#


## Number Number Number Number Number Number -> Number
## Takes dates (y1, m1, d1) and (y2, m2, d2) and returns (2) - (1) in days.
## def daysBetweenDates(y1, m1, d1, y2, m2, d2): return 0                   #stub
def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    days = 0
    ## Add days between y1 and y2
    if (y1 != y2):
        days = days + daysBtwYears(y1, y2)
    elif isLeap(y1):
        days = days + 1
        
    ## Add (positive or negative) days between m1 and m2
    if m1 != m2:
        days = days + daysBtwMonths(m1, m2)
    # Fix **possible** error on leap year. m1 after, or m2 before february, substracts one day each.
    if isLeap(y1) and m1 > 2: days = days - 1
    if isLeap(y2) and m2 < 2: days = days - 1

    ## Add (positive or negative) difference between days
    days = days + d2 - d1
        # Fix **possible** error on leap year, and february. m2 before 29, substracts one day.
    if isLeap(y2) and m2 == 2 and m2 < 29: days = days - 1

    return days


## Number -> Boolean
## Takes a number representing a year, and returns true if its leap, and false if not.
## def isLeap(y): return True                                              #stub
def isLeap(y):
    ## Is leap if is divisible by 4 and not by 100. Unless is divisible by 400.
    return (y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0)


## Number Number -> Number
## Takes two years, and returns the number of days between them. Assuming same MM and DD
## def daysBtwYears(y1, y2): return 0                                      #stub
def daysBtwYears(y1, y2):
    d = 0
    d = (y2 - y1) * 365
    for i in range (y1, y2+1):
        if isLeap(i):
            d = d + 1
    return d

## Number Number -> Number
## Takes two months and returns the number of days between m1 and m2-1
##def daysBtwMonths(m1, m2): return 0                                     #stub
def daysBtwMonths(m1, m2):
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d = 0
    for i in range (m1 - 1, m2 - 1):
        d = d + monthDays[i]
    ## if m2 happens before m1, return a negative number
    if m2 < m1: return 0 - d
    return d