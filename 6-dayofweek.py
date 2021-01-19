def day2dayOfWeek(nDay):
    aDays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday"]
    return aDays[nDay - 1]

try:
    nDay = int(input("Enter a day of the week ... 1 for Sunday: "))
    sDayOfWeek = day2dayOfWeek(nDay)
    print("The", nDay, "of the week is", sDayOfWeek)
except:
    print("please enter a day from 1-7")