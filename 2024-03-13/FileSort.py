fileHandle = open("2024-03-13/Numbers.txt", "r")
Array = [None for i in range(5)]

for i in range(5):
    fileText = fileHandle.readline().strip()
    Array[i] = int(fileText)

Counter = len(Array) - 1
while True:

    Swap = False

    for i in range(Counter):
        if Array[i] > Array[i + 1]:
            Temp = Array[i]
            Array[i] = Array[i + 1]
            Array[i + 1] = Temp
            Swap = True

    Counter = Counter - 1

    if Counter == 0 or Swap == False: break

for i in range(len(Array)):
    print(Array[i])