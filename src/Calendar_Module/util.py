# rember the methods
def to_ow_day():
    import calendar

    month, date, year = map(int, input().split())

    d = calendar.weekday(year, month, date)
    print(d)
    print(calendar.day_name[d].upper())
