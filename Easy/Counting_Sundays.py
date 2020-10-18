from enum import IntEnum


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return True
    return False


month_days = {"jan": 31, "feb": 28, "march": 31, "april": 30, "may": 31, "june": 30, "july": 31,
              "aug": 31, "sept": 30, "oct": 31, "nov": 30, "dec": 31}


class WeekDays(IntEnum):
    Mon = 1
    Tue = 2
    Wed = 3
    Thur = 4
    Fri = 5
    Sat = 6
    Sun = 7


count = 0
month = 'jan'
year = 1900

current_day = WeekDays(1)
while year <= 2000:
    for month in month_days:
        if year > 1900 and current_day == WeekDays.Sun:
            count += 1
            print(f"Found {count} on {current_day, month, year}")
        # print(current_day, month, year)
        if month == 'feb' and is_leap_year(year):
            days = month_days[month] + 1
        else:
            days = month_days[month]
        new_day = WeekDays((int(current_day)-1 + days) % 7 + 1)
        current_day = new_day
    year += 1
