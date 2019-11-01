lineCount: int = 0
wordCount: int = 0
charCount: int = 0
with open("test.txt",'r') as file:
    for line in file:
        print(line, end='')
        lineCount += 1
        for c in line:
            charCount += 1
        for word in line.split():
            wordCount += 1
            #print(i)

print("\nNo of lines- ", lineCount)
print("No of words- ", wordCount)
print("No of characters- ", charCount)

