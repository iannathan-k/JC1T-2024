studentNames = ["" for i in range(10)]
test1Scores = [0 for i in range(10)]
test2Scores = [0 for i in range(10)]
testsAvg = [0.0 for i in range(10)]

for i in range(10):
    testsAvg[i] = (test1Scores[i] + test2Scores[i]) / 2

# find a student and output the average
# find the highest average and output the name
# find the lowest average and output the name
# count the number of students who scored above the class avg
# no. of students who passed or failed