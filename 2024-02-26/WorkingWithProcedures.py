def printMyName():
    print("My name is Ian")

printMyName()



def sayHello(name):
    print("Hello", name)

sayHello("Ian")



def addTwoNumbers(num1, num2):
    sum = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum}")

firstNum = int(input("Please enter the first num: "))
secondNum = int(input("Please enter the second num: "))
addTwoNumbers(firstNum, secondNum)