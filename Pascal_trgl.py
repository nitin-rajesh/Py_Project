def fact(n):
    if n <= 1:
        return 1
    return fact(n-1)*n

def C(n,r):
    return int(fact(n)/(fact(n-r)*fact(r)))

def pascal(rows):
    for i in range(0,rows):
        for x in range(0, (rows - i - 1)*2):
            print(' ', end = '')
        for j in range(0,i+1):
            print(C(i,j),'  ', end = '')
        print('\n')

num = int(input("How many rows\n"))
pascal(num)