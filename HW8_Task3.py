def shorten_to_date(long_date):
    date, time = long_date.split(",")
    return date

print(shorten_to_date("Monday February 2, 8pm"))