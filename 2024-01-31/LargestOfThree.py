NumA = int(input("Please enter num 1: "))
NumB = int(input("Please enter num 2: "))
NumC = int(input("Please enter num 3: "))

if NumA > NumB:
    if NumA > NumC:
        print(str(NumA) + ", The first number is greatest")
    else:
        print(str(NumC) + ", The third number is greatest")
elif NumB > NumC:
    print(str(NumB) + ", The second number is greatest")
else:
    print(str(NumC) + ", The third number is greatest")