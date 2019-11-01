def remN(listOfStuff, element, n):
    indexList = []
    pos: int = 0
    occ: int = 0
    for i in listOfStuff:
        if i == element:
            indexList.append(pos)
            occ += 1
        pos += 1
    if occ == 0:
        print("Element not found")
        return
    if occ < n:
        if occ == 1:
            print("There is only one occurrence")
            return
        print("There are only", occ, "occurences")
        return
    pos = indexList[n-1]
    listOfStuff.pop(pos)

firstList = []
num = int(input('How many things\n'))
print('Enter ', num, ' things')
i = 0
while i < num:
    word = input()
    firstList.append(word)
    i += 1
element = input("What to remove? ")
n = int(input("Which occurrence "))
remN(firstList,element,n)
print(firstList)