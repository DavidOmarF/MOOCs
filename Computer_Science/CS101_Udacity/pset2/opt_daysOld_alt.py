# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#
from datetime import datetime

## Number Number Number Number Number Number -> Number
## Takes dates (y1, m1, d1) and (y2, m2, d2) and returns (2) - (1) in days.
## def daysBetweenDates(y1, m1, d1, y2, m2, d2): return 0                   #stub
def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    # Convert received data to datetime type
    date1 = datetime.strptime(str(m1).zfill(1) + str(d1) + str(y1), '%m%d%Y')
    date2 = datetime.strptime(str(m2).zfill(1) + str(d2) + str(y2), '%m%d%Y')
    return (date2 - date1).days
