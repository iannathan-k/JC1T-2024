studentNames = ["" for i in range(10)]
test1Scores = [0 for i in range(10)]
test2Scores = [0 for i in range(10)]
testsAvg = [0.0 for i in range(10)]

highest = -1
highestName = ""
lowest = 101
lowestName = ""
passed = 0
failed = 0

for i in range(10):
    testsAvg[i] = (test1Scores[i] + test2Scores[i]) / 2

    if testsAvg[i] >= 50:
        passed = passed + 1
    else:
        failed = failed + 1
    
    if testsAvg[i] > highest:
        highest = testsAvg[i]
        highestName = studentNames[i]
    
    if testsAvg[i] < lowest:
        lowest = testsAvg[i]
        lowestName = studentNames[i]

print(f"the number of students who passed is {passed} and failed is {failed}")
print(f"the highest scoring student is {highestName} at {highest}")
print(f"the lowest scoring student is {lowestName} at {lowest}")

# find a student and output the average
# find the highest average and output the name
# find the lowest average and output the name
# count the number of students who scored above the class avg
# no. of students who passed or failed