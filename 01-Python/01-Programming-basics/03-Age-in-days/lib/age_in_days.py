from datetime import datetime

def age_in_days(year, month, days):

    current_date = datetime.today()

    birthday_date = datetime(year, month, days)

    difference = current_date - birthday_date

    return difference.days

print(age_in_days(2003, 8, 26))


