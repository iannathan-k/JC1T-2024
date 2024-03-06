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

TestScores = [[67, 78],
              [88, 79],
              [66, 59],
              [99, 81],
              [77, 92]]

StudentNames = ["Alex", "John", "Ian", "Irin", "Aileen"]

for i in range(len(TestScores)):
    print(StudentNames[i], TestScores[i][0], TestScores[i][1])