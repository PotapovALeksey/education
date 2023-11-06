from datetime import date, timedelta
from collections import defaultdict

WEEKDAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
SATURDAY = 5
SUNDAY = 6
WEEKENDS = {SATURDAY, SUNDAY}

def is_birthday_in_current_week(birthday: date, start_date: date, end_date: date):
    return start_date <= birthday <= end_date


def get_birthdays_per_week(users):
    
    birthdays = defaultdict(list)

    start_date = date.today()
    end_date = start_date + timedelta(days=6)

    for user in users:

        birthday = user['birthday']
        current_year_birthday_date = start_date.replace(month=birthday.month, day=birthday.day)
        next_year_birthday_date = start_date.replace(year=start_date.year + 1, month=birthday.month, day=birthday.day)

        if is_birthday_in_current_week(current_year_birthday_date, start_date, end_date) or is_birthday_in_current_week(next_year_birthday_date, start_date, end_date):

            if current_year_birthday_date.weekday() in WEEKENDS:
                next_monday_date = current_year_birthday_date + timedelta(days=2 if current_year_birthday_date.weekday() == SATURDAY else 1)

                if next_monday_date <= end_date:
                    birthdays['Monday'].append(user['name'])

            else:
                birthdays[WEEKDAYS[current_year_birthday_date.weekday()]].append(user['name'])

    return dict(birthdays)


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": date(1976, 1, 1)},
        {"name": "John Koum", "birthday": date(1976, 1, 1)},
        {"name": "Ivan Koum", "birthday": date(1976, 1, 1)},
        {"name": "Fedor Koum", "birthday": date(1976, 11, 3)},
        {"name": "Alex Koum", "birthday": date(1976, 11, 4)},
        {"name": "Peter Koum", "birthday": date(1976, 11, 5)},
        {"name": "Stepan Koum", "birthday": date(1976, 11, 6)},
        {"name": "Fedor Koum", "birthday": date(1976, 11, 7)},
        {"name": "Igor Koum", "birthday": date(1976, 11, 7)},
        {"name": "Stepan Koum", "birthday": date(1976, 11, 8)},
        {"name": "Liza Koum", "birthday": date(1976, 11, 9)},
        {"name": "Dima Koum", "birthday": date(1976, 11, 10)},
    ]
    
    result = get_birthdays_per_week(users)

    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
