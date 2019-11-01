def trimIt(listWithDuplicates):
    originalList = []
    for word in listWithDuplicates:
        if word not in originalList:
            originalList.append(word)
    return originalList

firstList = []
num = int(input('How many things\n'))
print('Enter ', num,' things')
i = 0
while i < num:
    word = input()
    firstList.append(word)
    i += 1
print("Old list", firstList)
newList = trimIt(firstList)
print("New list", newList)
