def count():
    odd = 0
    even = 0
    num = int(input("Please enter first num: "))
    while num != 99:
        if num % 2 == 1:
            odd = odd + 1
        else:
            even = even + 1
        num = int(input("Please enter next num: "))
    print(f"the number of odd is {odd} and even is {even}")


count()