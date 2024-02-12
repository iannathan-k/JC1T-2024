Array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
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