import datetime

def get_days_from_today(date):
    try:
        now = datetime.datetime.today().date()
        print("Now is: ", now)
        formatted_user_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        print("Entered date is: ", formatted_user_date)
        dates_delta = (now - formatted_user_date).days
        print("Differnce is: ", dates_delta)

    except (TypeError, ValueError):
        print("Enter date in format YYYY-MM-DD")
get_days_from_today("2024-07-05")

