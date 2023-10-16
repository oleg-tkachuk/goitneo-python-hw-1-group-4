from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    birthday_dict = defaultdict(list)
    today = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            delta_days = (birthday_this_year - today).days

        day_of_week = (today + timedelta(days=delta_days)).strftime("%A")
        birthday_dict[day_of_week].append(name)

    for day, names in birthday_dict.items():
        print(f"{day}: {', '.join(names)}")

users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
    {"name": "Jill Valentine", "birthday": datetime(1977, 11, 20)},
    {"name": "Test User 1", "birthday": datetime(2023, 10, 14)},
    {"name": "Test User 2", "birthday": datetime(1980, 10, 21)}
]

get_birthdays_per_week(users)
