def Fibonacci(num,n):
    lst = []
    a,b = 1,1
    if (n == 1):
        lst.append(1)
        return sum(lst)
    elif (n == 2):
        lst.append(1)
        lst.append(1)
        return sum(lst)
    else:
        for i in range(2,n):
            num.append(num[-1]+num[-2])
        return num[-1]





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


