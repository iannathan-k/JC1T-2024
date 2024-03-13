fileHandle = open("2024-03-13/TextFile.txt", 'w')

# fileHandle.write("I am the best\n")
# fileHandle.write("Nobody compares to me\n")
# fileHandle.write("VIIO")

for i in range(10):
    fileHandle.write("Hello World\n")

fileHandle.close()

fileHandle = open("2024-03-13/TextFile.txt", "r")

for i in range(5):
    fileText = ["", "", "", "", ""]
    fileText[i] = fileHandle.readline().strip()
fileHandle.close()

print(fileText)