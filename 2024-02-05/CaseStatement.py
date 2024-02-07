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

match userDay:
    case 1 : print(str(userDay), "is Sunday")
    case 2 : print(str(userDay), "is Monday")
    case 3 : print(str(userDay), "is Tuesday")
    case 4 : print(str(userDay), "is Wednesday")
    case 5 : print(str(userDay), "is Thursday")
    case 6 : print(str(userDay), "is Friday")
    case 7 : print(str(userDay), "is Saturday")
    case _: print("Invalid Number")