def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 400 != 0:
        return False
    elif year % 100 != 0: 
        return True
    else:
        return True
    
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
def days_in_month(year, month):
    if year < 1 or year < 1582 or month >12:
        return None
    if is_year_leap(year):
        days[1] = 29
    return days[month-1]

def day_of_year(year, month, day):
    total = 0
    for i in range(1,month):        #you want first month to be 1
      d = days_in_month(year, i)
      total += d
    d = days_in_month(year, month)
    if day >= 1 and day <= d:
      total = total + day
    else:
        return None
    return total

print(day_of_year(2000, 12, 31))
