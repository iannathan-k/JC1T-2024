def addTwoNumbers(num1, num2):
    sum = num1 + num2
    return sum  

firstNum = int(input("Enter first num: "))
secondNum = int(input("Enter second num: "))

tempSum = addTwoNumbers(firstNum, secondNum)
print(f"The sum of {firstNum} and {secondNum} is {tempSum}")

# def fact(prod, num):
#     prod = prod * num
#     num -= 1
#     if num == 0: 
#         return prod
#     else:
#         return fact(prod, num)

def fact(num):
    prod = 1
    for i in range(1, num + 1):
        prod = prod * i
    return prod

print(fact(5))