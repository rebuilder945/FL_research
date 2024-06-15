def myprime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n == 3:
        return True
    elif n == 9:
        return False
    elif n == 27:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
            return True

lstA = eval(input())
lstB = []
for x in lstA:
    if myprime(x):
        lstB.append(x)

print(lstB)

