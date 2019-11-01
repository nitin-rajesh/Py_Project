def caseCount(word):
    lowerCount: int = 0
    upperCount: int = 0
    for alphabet in word:
        #print(ord(i))
        #lower case from 97 to 122
        #upper case from 65 to 90
        if ord(alphabet) >= 65 and ord(alphabet) <= 90:
            upperCount += 1
        if ord(alphabet) >= 97 and ord(alphabet) <= 122:
            lowerCount += 1
    array = [upperCount,lowerCount]
    return array


#main function starts here
word: str = input("Enter a string: \n")
array = caseCount(word)
print("Number of capital letters: ", array[0])
print("Number of lower case letters: ", array[1])