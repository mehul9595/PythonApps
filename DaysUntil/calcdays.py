import datetime

def header():
    print("--------------------------------")
    print("App to Calculate days until...")
    print("--------------------------------")

def get_birthday():
    print("Enter your birthday:")
    year = int(input("year: "))
    month = int(input("month: "))
    day = int(input("day: "))
    birthdate = datetime.date(year, month, day)
    return birthdate

def compare_date(original_date, target_date):
    daysUntil =  original_date - target_date
    return daysUntil.days

def main():
    header()
    birthday = get_birthday()
    today = datetime.date.today()
    daysUntil = compare_date(birthday, today)
    print("Your birthdate is {}".format(birthday))
    print("Today is: ", today)
    print("Diff is {} days.".format(daysUntil))


if __name__ == "__main__":
    main()
