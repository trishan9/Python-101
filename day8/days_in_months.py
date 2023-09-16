month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  is_leap_year = is_leap(year)  
  total_days = month_days[month - 1]
  if is_leap_year and month == 2:
    total_days += 1
  return total_days
  
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)