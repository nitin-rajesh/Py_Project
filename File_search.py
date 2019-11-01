keyWord = input("Enter word to search\n")
occurrences: int = 0
with open('test.txt','r') as file:
    for line in file:
        for word in line.split():
            if word == keyWord:
                occurrences += 1

print("This word has occurred",occurrences,"times")