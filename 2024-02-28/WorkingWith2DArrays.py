marks = [[0 for i in range(5)],
         [0 for i in range(5)],
         [0 for i in range(5)],
         [0 for i in range(5)],
         [0 for i in range(5)],
         [0 for i in range(5)],
         [0 for i in range(5)],
         [0 for i in range(5)],
         [0 for i in range(5)],
         [0 for i in range(5)]]

for i in range(10):
    for j in range(5):
        marks[i][j] = i + 1

for i in range(10):
    print(marks[i][0])