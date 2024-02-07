StudentNames = [None] * 10

for i in range(10):
    name = input("Enter in student name: ")
    StudentNames[i] = name

for i in range(len(StudentNames)):
    print(StudentNames[i])

Name = input("Please enter student to search: ")
Found = False
Index = 0
while Found == False and Index < len(StudentNames):
    if StudentNames[Index] == Name:
        Found = True
        print(f"Student {Name} found at index {Index}")
    Index = Index + 1

if Found == False: print(f"Student {Name} not found")