def recFib(x):
    if x <= 0:
        return 0
    if x == 1:
        return 1
    return recFib(x-1) + recFib(x-2)

x = int(input("How many Fibonacci numbers?\n"))
for i in range(1,x+1):
    print(recFib(i),end = '    ')
    if i % 20 == 0:
        print('')

