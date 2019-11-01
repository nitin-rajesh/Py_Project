numList = []
num = int(input('How many things\n'))
print('Enter ', num,' things')
i = 0
while i < num:
    num = int(input())
    numList.append(num)
    i += 1

numList.sort()
print("Second largest element: ",numList[-2])