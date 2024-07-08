import datetime

def get_upcoming_birthdays(users):
    current_date = datetime.datetime.today().date()
    max = current_date + datetime.timedelta(days=6)
    current_year = current_date.year
    list_of_birthdays = []



    for user in users:
        birthday = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        next_birthday = datetime.date(current_year, birthday.month, birthday.day)

        if next_birthday < current_date:
            next_birthday =datetime.date(current_year + 1, birthday.month, birthday.day)
        
        if next_birthday.weekday() == 5:
            next_birthday += datetime.timedelta(days=2)

        if next_birthday.weekday() == 6:
            next_birthday += datetime.timedelta(days=1)

        if next_birthday <= max and next_birthday >=current_date:
            list_of_birthdays.append({"name":user["name"], "congratulation_date": next_birthday.strftime("%Y.%m.%d")})

    return list_of_birthdays

        

print(get_upcoming_birthdays([{"name": "John Doe", "birthday": "1985.07.13"}, {"name": "Jane Smith", "birthday": "1990.07.15"}]))