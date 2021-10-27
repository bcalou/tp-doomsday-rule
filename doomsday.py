# Ask the user for a date until the input is valid
while True:
    date: str = input("Please enter a YYYY-MM-DD date\n-> ")
    if is_valid_date(date):
        break

print(get_day_for_date(date))