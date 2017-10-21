daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    if year%4 !=0:
        return False
    elif year%100 !=0:
        return True
    elif year%400 !=0:
        return False
    else:
        return True
        
def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    years = y2 - y1
    monthDifference = abs(m2 - m1)
    return days
        
print(isLeapYear(1996))