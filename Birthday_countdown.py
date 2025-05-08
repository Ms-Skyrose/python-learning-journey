from datetime import date

def birthday_countdown():
    today = date.today()
    current_year = today.year
    birthday = date(current_year, 6, 12)

    if today > birthday:
        next_year = current_year + 1
        birthday = date(next_year, 6, 12)
    
    days_left = (birthday - today).days
    print(f"Days left until your birthday: {days_left}")
    print(f"Your birthday is on {birthday.strftime('%B %d, %Y')} and ie. {birthday.strftime("%A")}.")
    print(f"Today is {today.strftime('%B %d, %Y')} and ie. {today.strftime("%A")}.")


if __name__ == "__main__":
    birthday_countdown()



