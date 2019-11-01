firstList = []
num = int(input('How many things\n'))
print('Enter ', num,' things')
i = 0
while i < num:
    word = input()
    firstList.append(word)
    i += 1

word = input("What to search for\n")
occ: int = firstList.count(word)
print("It occured",occ,"times")