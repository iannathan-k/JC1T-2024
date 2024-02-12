Sum = 0
for i in range(10):
    Num = int(input())
    Sum = Sum + Num

print(f"sum is {Sum}")

Sum = 0
Counter = 0
while Counter < 10:
    Num = int(input())
    Sum = Sum + Num
    Counter += 1

print(f"sum is {Sum}")

Sum = 0
Num = int(input())
while Num != -999:
    if Num > 0:
        sum = sum + Num
    Num = int(input())

print(Sum)