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
        return listOfStuff
    if occ < n:
        if occ == 1:
            print("There is only one occurrence")
            return listOfStuff
        print("There are only", occ, "occurences")
        return listOfStuff
    pos = indexList[n-1]
    #print(pos)
    newStuff = listOfStuff[:pos] + listOfStuff[pos+1:]
    return newStuff

word = input("Enter a string\n")
element = input("Which letter to remove? ")
n = int(input("Which occurrence "))
word = remN(word,element,n)
print(word)
