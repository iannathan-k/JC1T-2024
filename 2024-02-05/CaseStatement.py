userDay = int(input("Please enter a number from 1-7: "))

if userDay == 1:
    print(str(userDay), "is Sunday")
elif userDay == 2:
    print(str(userDay), "is Monday")
elif userDay == 3:
    print(str(userDay), "is Tuesday")
elif userDay == 4:
    print(str(userDay), "is Wednesday")
elif userDay == 5:
    print(str(userDay), "is Thursday")
elif userDay == 6:
    print(str(userDay), "is Friday")
elif userDay == 7:
    print(str(userDay), "is Saturday")
else:
    print(str(userDay), "Invalid Number")

day = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday"
}

if userDay in day:
    print(str(userDay), "is", day[userDay])
else:
    print("Number is not between 1 and 7!")