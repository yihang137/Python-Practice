print("Welcome to your daily exercise !")

total_minutes = 0

for day in range(1, 6):
    minutes = float(input("How many minutes did you exercise on day {}? ".format(day)))
    total_minutes += minutes

    if minutes == 0:
        print("You didn’t exercise at all on day {}. Let’s try to move more!".format(day))
    elif minutes < 30:
        print("You exercised a bit on day {}. Keep pushing!".format(day))
    elif 30 <= minutes <= 60:
        print("Great job exercising on day {}!".format(day))
    else:
        print("Awesome! You went above and beyond on day {}!".format(day))

average = total_minutes / 5

print("In total, you exercised for {:.1f} minutes over 5 days, averaging {:.1f} minutes per day.".format(total_minutes, average))

if average < 30:
    print("Try to exercise at least 30 minutes a day for better health.")
elif average == 30:
    print("You’re hitting the recommended 30 minutes daily goal. Well done!")
else:
    print("You’re exceeding the daily exercise recommendation. Keep it up!")